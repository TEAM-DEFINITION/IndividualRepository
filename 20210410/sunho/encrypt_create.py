import cryption

in_str = input(" 암호화 할 값을 입력하세요\n")


if in_str != None:

    in_enc = cryption.MyCipher().encrypt_str( in_str )     #  암호화

    print( in_enc )


    print( "입력된 값: ", cryption.MyCipher().decrypt_str(in_enc) )    # 복호화