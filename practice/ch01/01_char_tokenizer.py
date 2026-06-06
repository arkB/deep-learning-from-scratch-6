class CharTokenizer:
    def encode(self, text):
        return [ord(char) for char in text]

    def decode(self, ids):
        return "".join([chr(i) for i in ids])


tokenizer = CharTokenizer()
text = "hello世界☺"

ids = tokenizer.encode(text)
print(ids)

decode = tokenizer.decode(ids)
print(decode)
