class Avatar:
    nick = ""
    vida = 0
    lvl = 0
    classe = "Humano"


class Avatar_config(Avatar):
    def setNick(self):
        a_nick = str(input("Digite o nome do personagem: "))
        self.nick = a_nick
        self.vida = 100

    setNick(Avatar)


