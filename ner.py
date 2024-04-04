
class Ner:
    """ ner classification class"""
    def __init__(self, llist, rlist):
        self.llist = llist
        self.rlist = rlist

    def binarysearch(self, xlist, item):
        """ binary search """
        self.xlist = xlist
        self.item = item
        low:int = 0
        high:int = len(self.xlist)-1
        while low <= high:
            mid:int = (low + high) // 2
            if self.xlist[mid] == self.item:
                return mid
            elif self.xlist[mid] < self.item:
                low = mid + 1
            elif self.xlist[mid] > self.item:
                high = mid - 1
        return False

    def load(self, text):
        """ ner method """
        self.text = text
        tlist = []
        slist = []
        vlist = []
        ngram = 2

        def fngrams(text, ngrams):
            """ function to make n-grams"""
            nlist = []
            for x, i in enumerate(self.text):
                trlist = []
                tc = ""
                for j in range(ngrams):
                    if j == 0:
                        tc = str(text[x + j])
                    elif j > 0:
                        try:
                            tc += " " + str(text[x + j])
                        except IndexError:
                            break
                    trlist.append(tc)
                nlist.append(trlist)
            return nlist

        ngtext = fngrams(self.text, ngram)
        
        for x, i in enumerate(ngtext):
            c = 0
            for j in i[::-1]:
                c += 1
                binaryr = self.binarysearch(self.llist, j)
                if binaryr != False:
                    slist.append(j)
                    vlist.append(self.rlist[binaryr])
                    break
                if c == len(i):
                    slist.append(i[0])
                    vlist.append("out")

        for x, j in enumerate(slist):
            if type(j) == int:
                if j > 0 and j <= 31:
                    if vlist[x + 1] == "date":
                        vlist[x] = "start-date"
                elif j > 1700 and j < 2030:
                    if vlist[x + 1] == "date":
                        if vlist[x - 1] != "date":
                            vlist[x] = "start-date"
                        else:
                            vlist[x] = "date"
                        vlist[x + 1] = "end-date"

        for k, l in zip(slist, vlist):
            tlist.append((k, l))
        return tlist
