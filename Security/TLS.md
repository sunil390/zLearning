# TLS ...

1. https://browserleaks.com/tls
2. [TLS 1.2 RFC](https://www.rfc-editor.org/rfc/rfc5246#section-7.4.2)
3. 7.4.1.4.1.  Signature Algorithms
```txt
   The client uses the "signature_algorithms" extension to indicate to
   the server which signature/hash algorithm pairs may be used in
   digital signatures.  The "extension_data" field of this extension
   contains a "supported_signature_algorithms" value.

If the client provided a "signature_algorithms" extension, then all
certificates provided by the server MUST be signed by a hash/signature
algorithm pair that appears in that extension.

Firefox
signature_algorithms
algorithms	
0x0403 ecdsa_secp256r1_sha256
0x0503 ecdsa_secp384r1_sha384
0x0603 ecdsa_secp521r1_sha512
0x0804 rsa_pss_rsae_sha256
0x0805 rsa_pss_rsae_sha384
0x0806 rsa_pss_rsae_sha512
0x0401 rsa_pkcs1_sha256
0x0501 rsa_pkcs1_sha384
0x0601 rsa_pkcs1_sha512
0x0203 ecdsa_sha1
0x0201 rsa_pkcs1_sha1
```
