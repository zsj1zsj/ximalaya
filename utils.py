from Crypto.Cipher import AES
import base64

# 使用 bytes.fromhex 将十六进制字符串转换为字节
key = bytes.fromhex("aaad3e4fd540b0f79dca95606e72bf93")


def decrypt_url(ciphertext):
    # Base64url 解码 (添加填充以确保长度为4的倍数)
    ciphertext_bytes = base64.urlsafe_b64decode(ciphertext + "==")

    # 创建 AES ECB 模式的密钥
    cipher = AES.new(key, AES.MODE_ECB)

    # 解密密文
    decrypted = cipher.decrypt(ciphertext_bytes)

    # 去除填充
    pad_len = decrypted[-1]
    decrypted = decrypted[:-pad_len]

    # 将字节转换为字符串
    return decrypted.decode('utf-8')