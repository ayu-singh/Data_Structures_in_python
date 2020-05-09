class StringRecurssion:

    def reverse(self, text):
        if len(text) == 0 or text == None:
            return None
        elif len(text) == 1:
            return text
        else:
            return self.reverse(text[1:]) + text[0]


    def permutation(self, text):
        out = []
        if text == None:
            return None
        elif len(text) <= 1:
            out = [text]
        else:
            for i_, letter in enumerate(text):

                for perm in self.permutation(text[:i_]+ text[i_+1:]):

                    out += [letter+perm]
        return out

    def list_element_reversal(self, l_text):
        if l_text == None:
            return None
        elif len(l_text) <= 1:
            return l_text
        else:
            return self.list_element_reversal(l_text[1:]) + [l_text[0]]


    def reverse_words(self, text):
        words = []
        i = 0
        while i < len(text):
            if text[i] != " ":
                start = i
                while i < len(text) and text[i] != " ":
                    i += 1
                words.append(text[start:i])

            i += 1
        return " ".join(self.list_element_reversal(words))

sr = StringRecurssion()
print(sr.reverse("well"))
print(sr.permutation("xyz"))
print(sr.reverse_words("good morning"))
