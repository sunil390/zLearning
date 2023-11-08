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
```
