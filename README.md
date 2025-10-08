# Caesar cipher suite

## Encrypt example

```
$ echo "flag{404_security_not_found}" | python3 caesar.py encrypt --offset 3 --shift 8
cahf{404_jndnclol_sli_mnlwe}
```

## Decrypt example

```
$ echo "cahf{404_jndnclol_sli_mnlwe}" | python3 caesar.py decrypt --offset 3 --shift 8
flag{404_security_not_found}
```

## Crack example

```
$ echo "cahf{404_jndnclol_sli_mnlwe}" | python3 caesar.py crack
flag{404_security_not_found}
```