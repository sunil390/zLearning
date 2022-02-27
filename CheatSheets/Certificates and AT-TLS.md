# Certificates and AT-TLS

## Server Authentication

1. Server sends certificate
2. Client verifies authenticity of server (local truststore, contains CA certificate)
3. Client sends userid + password over encrypted connection

## Client Authentication

1. Server sends certificate
2. Client verifies authenticity of server (local truststore, contains CA certificate)
3. Client sends certificate
4. Server verifies client certificate against RACF (or equivalent)
5. Server maps client certificate to a userid (no transmission of userid + password)

## TCPIP and PAGENT setup

### PAGENT STC

```jcl
STDENV DD
```

### Environment variables

```sh
PAGENT_CONFIG_FILE=...
PAGENT_LOG_FILE=...
```

### Configuration file

```sh
LogLevel 256
TcpImage...
TTLSConfig ...
```

### AT-TLS policy filerules for certificates, keyrings etc.

```sh

TTLSRule DBC1SecureServer
{
    LocalAddr ALL
    RemoteAddr ALL
    LocalPortRange 4840-4840
    Direction Inbound
    Jobname DBC1DIST
    TTLSGroupActionRef DB2SecureGrpAct
    TTLSEnvironmentActionRef DB2SecureEnvAct
    TTLSConnectionActionRef DB2SecureConAct
}
TTLSGroupAction DB2SecureGrpAct
{
    TTLSEnabled On
    Trace 31
}

TTLSEnvironmentAction DB2SecureEnvAct
{
    Trace 31
    TTLSKeyRingParms
    {
        Keyring DBC1KEYRING
    }
    HandShakeRole Server
    TTLSEnvironmentAdvancedParms
    {
    TLSv1.2 On
    }
}

TTLSConnectionAction DB2SecureConAct
{
    TTLSConnectionAdvancedParms
    {
        CertificateLabel DBC1CERT
    }
}

Client Authentication


TTLSEnvironmentAction DB2SecureEnvAct
{
    Trace 31
    TTLSKeyRingParms
    {
        Keyring DBC1KEYRING
    }
    HandShakeRole ServerWithClientAuth
    ClientAuthType SAFCheck
    TTLSEnvironmentAdvancedParms
    {
    TLSv1.2 On
    }
}
```

## RACF Certificates

### CA Certificate

```sh
RACDCERT CERTAUTH GENCERT –
    SUBJECTDSN(OU('IDUG CA')-
    O('IDUG')-
    L('ZOS')-
    SP('EDINBURGH') –
    C('UK') -
    NOTAFTER(DATE(2025-12-31)) –
    WITHLABEL('IDUG CA CERT') –
    KEYUSAGE(CERTSIGN)

RACDCERT CERTAUTH –
    EXPORT(LABEL('IDUG CA CERT'))-
    DSN('ADMIN.TLS.CACERT')
```

### Server Certificate signed with CA Certificate

```sh
RACDCERT ID(DBC1STC) GENCERT –
    SUBJECTDSN(CN('DBC1.ZOS.IDUG.ORG')-OU('DBC1STC')-
    O('IDUG') -
    L('ZOS')-
    SP('EDINBURGH') –
    C('UK') –
    ALTNAME(IP(10.3.20.125)) -
    NOTAFTER(DATE(2025-12-31)) –
    WITHLABEL('DBC1CERT') –
    SIGNWITH(CERTAUTH LABEL('IDUG CA CERT'))
```

### Add Certificates to Keyring

```sh
RACDCERT ID(DBC1STC) ADDRING(DBC1KEYRING)
Cert#1
RACDCERT ID(DBC1STC) CONNECT(CERTAUTH -
    LABEL('IDUG CA CERT') RING(DBC1KEYRING))
Cert#2
RACDCERT ID(DBC1STC) CONNECT(ID(DBC1STC)-
    LABEL('DBC1CERT') RING(DBC1KEYRING) DEFAULT)

PERMIT IRR.DIGTCERT.LIST CLASS(FACILITY) -
    ID(DBC1STC) ACCESS(READ)
PERMIT IRR.DIGTRING.LIST CLASS(FACILITY) –
    ID(DBC1STC) ACCESS(READ)

Client Authentication, Export Client Certificate from Java/GSKit KeyStore
-------------------------------------------------------------------------

FTP client certificate to z/OS in text format to a sequential file with RECFM=VB

RACDCERT -
    ADD('<data set name>') ID(DB2USR1) TRUST -
    WITHLABEL('DB2CLIENTCERT')
Cert#3
RACDCERT ID(DBC1STC) CONNECT(ID(DB2USR1)) -
    LABEL('DB2CLIENTCERT') -
    RING(DBC1KEYRING) 

```

## Java KeyStore/Trust Store - For JDBC and REST Calls

1. Keystore: client certificates and private keys
2. Truststore: CA certificates
3. Java keytool (part of JRE) for administration of keystores, truststores and certificates

### create a truststore with private key

```sh
cd C:\Program Files\Java\jre1.8.0_321\bin
keytool –genkeypair –keystore mykeystore –storepass mykeypass<Prompts for X.509 distinguished name> 
```

### Import CA certificate into truststore

```sh
keytool –importcert –keystore mykeystore –storepass mykeypass –file CAcert.crt –trustcacerts –alias "IDUG CA CERT"
```

### List contents of truststore

```sh
keytool –list –keystore mykeystore –storepass mykeypass 
keytool –list –keystore mykeystore –storepass mykeypass –alias "IDUG CA CERT"
```

## ODBC/CLI - GSKit Keystore - shipped with Db2 Clients and Db2 Data Server Drivers

### create keystore and "stash" file (stores keystore password)

```sh
gsk8capicmd_64 -keydb -create –db "mykeydb.kdb" –pw "mykeypass" –type cms –stash –fips
```

###  Import CA certificate

```sh
gsk8capicmd_64 –cert –add –db "mykeydb.kdb" –pw "mykeypass" –file "zos_ca.crt" –label "IDUG CA CERT" –format ascii
```

### List keystore contents

```sh
gsk8capicmd_64 –cert –list –db "mykeydb.kdb" –pw "mykeypass"
gsk8capicmd_64 –cert –details –db "mykeydb.kdb" –pw "mykeypass" –label "IDUG CA CERT"
```

