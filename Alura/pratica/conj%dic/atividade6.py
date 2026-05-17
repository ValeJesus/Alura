class Alteratudo:

    equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}

    equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}

    def coletar_dado(self):
        print("\nProcedimentos disponíveis:")
        print(self.equipe_a.union(self.equipe_b))

        self.remove = input(
            "\nDigite o procedimento que deseja remover "
            "(escreva 'sair' para parar): "
        )

    def verificar(self):

        while self.remove != 'sair':

            if self.remove in self.equipe_a:
                self.equipe_a.remove(self.remove)
                print(f"\n'{self.remove}' removido da equipe A")

            elif self.remove in self.equipe_b:
                self.equipe_b.remove(self.remove)
                print(f"\n'{self.remove}' removido da equipe B")

            else:
                self.erro()

            print("\nConjunto atualizado:")
            print(self.equipe_a.union(self.equipe_b))

            self.remove = input(
                "\nDigite outro procedimento "
                "(ou 'sair' para encerrar): "
            )

        print("\nPrograma encerrado.")

    def erro(self):
        print(
            "\nVocê digitou errado ou o procedimento não existe.\n"
        )

    def main(self):
        self.coletar_dado()
        self.verificar()


if __name__ == '__main__':

    executar = Alteratudo()
    executar.main()