import random


class Mob:
    nome = ""
    vida = 0
    classe = ""
    habilidade = []
    detalhe = ""
    mob_list = ["Covid-19",
                "Vírus de Marburg",
                "Ebola",
                "Hantavírus",
                "H5N1",
                "Lassa",
                "Junin",
                "Crimeia-Congo",
                "Machupo",
                "Kyansur",
                "Dengue"
                ]

class List_mobs(Mob):
    def set_mob(self):
        mob_spawn = random.choice(self.mob_list)
        self.nome = mob_spawn

    def set_mob_atributos(self):
        
        # Covid-19 
        if self.nome == "Covid-19":
            self.vida = "?" # nao definido
            self.classe = "Vírus Desconhecido"
            self.habilidade.append("Multiplicar")
            self.detalhe = "A Covid-19 é uma infecção respiratória aguda causada pelo coronavírus SARS-CoV-2, potencialmente grave, de elevada transmissibilidade e de distribuição global."

        # Degue
        elif self.nome == "Dengue":
            self.vida = 100
            self.classe = "Virus Comum"
            self.habilidade.append("Desorientar")
            self.detalhe = "Doença viral transmitida por mosquitos que ocorre em áreas tropicais e subtropicais."

        # Kyansur
        elif self.nome == "Kyansur":
            self.vida = 150
            self.classe = "Vírus Comum"
            self.habilidade.append("Camuflar") 
            self.detalhe = "Cientistas descobriram o vírus da floresta de Kyansur na costa sudoeste da Índia em 1955."

        # Machupo
        elif self.nome == "Machupo":
            self.vida = 150
            self.classe = "Vírus bovinico"
            self.habilidade.append("Confusão")
            self.detalhe = "O vírus Machupo está associado à febre hemorrágica boliviana."

        # Crimeia-Congo
        elif self.nome == "Crimeia-Congo":
            self.vida = 200
            self.classe = "Vírus comum"
            self.habilidade.append("Aftalizar") 
            self.detalhe = "O vírus da Crimeia-Congo é transmitido por carrapatos."
        
        # Junin
        elif self.nome == "Junin":
            self.vida = 250
            self.classe = "Vírus Desconhecido"
            self.habilidade.append("Sobreaquecer") 
            self.detalhe = "O vírus da Crimeia-Congo é transmitido por carrapatos." 

        # Lassa
        elif self.nome == "Lassa":
            self.vida = 300
            self.classe = "Vírus comum"
            self.habilidade.append("Desaparecer") 
            self.detalhe = "Uma enfermeira na Nigéria foi a primeira pessoa a ser infectada pelo vírus de Lassa." 
        
        # H5N1
        elif self.nome == "H5N1":
            self.vida = 350
            self.classe = "Vírus Perigoso"
            self.habilidade.append("Espalhar") 
            self.detalhe = "Os vários tipos de vírus da gripe aviária costumam causar pânico, o que talvez seja justificado pela taxa de mortalidade, que é de 70%."

        # Hantavírus
        elif self.nome == "Hantavírus":
            self.vida = 400
            self.classe = "Vírus aquatico"
            self.habilidade.append("Enxarcar") 
            self.detalhe = "O termo hantavírus refere-se a diversos tipos de vírus, o nome vem de um rio."

        # Ebola
        elif self.nome == "Ebola":
            self.vida = 450
            self.classe = "Vírus Perigoso"
            self.habilidade.append("Espalhar o caos") 
            self.detalhe = "Vírus surgido na África, ao todo existem 5 tipos."

        # Vírus de Marburg
        elif self.nome == "Vírus de Marburg":
            self.vida = 500
            self.classe = "Vírus super perigoso"
            self.habilidade.append("Destroçar") 
            self.detalhe = "O vírus mais perigoso do mundo!"

    def getMob(self):
        print(f'''
        Nome: {Mob.nome}               Vida: {Mob.vida}
        classe: {Mob.classe}            
        
        ''')
