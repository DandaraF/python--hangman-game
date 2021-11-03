class Replace:

    def muliple_replace(self, text):
        text = str(text)
        for char in "[]()',":
            text = text.replace(char, "")
        return text.strip()
