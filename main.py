from database import criar_tabela
import backend

def menu():
    criar_tabela()
    while True:
        print()
        print("O que deseja ?")
        print()
        opcao=(input("1 - Adicionar aluno\n2 - Listar todos os alunos\n3 - Atualizar dados de um aluno\n4 - Remover um aluno\n5 - Sair\nEscolha: "))

        if opcao == "1":
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Idade: "))
            curso = input("Curso: ")
            backend.adicionar_aluno(nome, idade, curso)
            print("Aluno cadastrado com sucesso!")

        elif opcao =="2":
            alunos = backend.listar_aluno()
            print("\n---Alunos Cadastrados---")
            for aluno in alunos:
                print (f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | Curso: {aluno[3]}")

        elif opcao=="3":
            id = int(input("ID do aluno: "))
            nome = input("Novo nome: ")
            idade = int(input("Nova idade: "))
            curso =(input("Novo curso: "))
            backend.atualizar_aluno(id,nome,idade,curso)
            print("Aluno atualizado com sucesso")

        elif opcao=="4":
            id=int(input("Entre com o ID: "))
            backend.remover_aluno(id)
            print("Aluno removido com sucesso")
        elif opcao=="5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")
menu()
