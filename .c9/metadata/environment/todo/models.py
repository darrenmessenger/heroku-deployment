{"filter":false,"title":"models.py","tooltip":"/todo/models.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":3,"column":0},"end":{"row":9,"column":24},"action":"insert","lines":["class Item(models.Model):","    ","    name = models.CharField(max_length=30, blank=False)","    done = models.BooleanField(blank=False, default=False)","","    def __str__(self):","        return self.name"],"id":2}],[{"start":{"row":9,"column":29},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":10,"column":0},"end":{"row":10,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":["t"],"id":4}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["."],"id":3},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["q"]},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["u"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["i"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":24},"end":{"row":9,"column":24},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1573076877187,"hash":"bb2ade0b5906d4c34ad5489e26929421fa78ce5e"}