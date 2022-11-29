# Security Policy

## Reporting

Thank you for taking the time to responsibly disclose any problems you find.

**Do not file public issues as they are open for everyone to see!**

All security vulnerabilities in `xor-cipher` should be reported by email
to [security@xor-cipher.com][Security Email].
Your report will be acknowledged within 24 hours, and you will receive a more
detailed response within 48 hours indicating the next steps in handling your report.

You can encrypt your report using our public key:
[`E236C27EBF7FD92F74FEDD09AE9C03A6C2E69001`][Security Key].
This key is also available on [MIT's Key Server][MIT Key Server]
and [reproduced below](#security-key).

After the initial reply to your report, the core team will try to keep you
informed of the progress being made towards a fix and official announcement.
These updates will be sent at least every five days. In reality, this is
more likely to be every 24-48 hours.

## Disclosure Policy

`xor-cipher` has a 5-step disclosure process:

1. The security report is received and is assigned a primary handler.
   This person will coordinate the fix and release process.

2. The problem is confirmed and a list of all affected versions is determined.

3. Code is audited to find any potential similar problems.

4. Fixes are prepared for all releases which are still under maintenance.
   These fixes are not committed to the public repository but rather
   held locally pending the announcement.

5. On the embargo date, the changes are pushed to the public repository
   and new builds are deployed.

This process can take some time, especially when coordination is required
with maintainers of other projects. Every effort will be made to handle
the issue in as timely a manner as possible, however it is important that
we follow the release process above to ensure that the disclosure is handled
in a consistent manner.

## Security Key

```text
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
zY6g3AC1qsvumpg/Hvo=
=TDA5
-----END PGP PUBLIC KEY BLOCK-----
```

## Attribution

This Security Policy is adapted from [Rust's Security Policy][Rust Security Policy].

[Security Email]: mailto:security@xor-cipher.com
[Security Key]: https://xor-cipher.com/keys/security
[MIT Key Server]: https://pgp.mit.edu/pks/lookup?op=index&search=0xE236C27EBF7FD92F74FEDD09AE9C03A6C2E69001
[Rust Security Policy]: https://rust-lang.org/policies/security
