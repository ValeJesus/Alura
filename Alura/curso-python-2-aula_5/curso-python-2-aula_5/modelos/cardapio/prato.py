
# Import da pasta modelos, pasta cardapio, arquivo item cardapio, class item cardapio
from modelos.cardapio.item_cardapio import ItemCardapio

# o (Item cardapio ) indica que o prato é uma classe filha do item cardapio
# A classe prato vai herdar metodos e atributos da classe item cardapio
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao

        def __str__(self):
            return self._nome