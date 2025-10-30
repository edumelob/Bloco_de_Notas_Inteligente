from note import Note
import json
import os

DATA_FILE = "data/notes.json"

def load_notes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return [Note.from_dict(n) for n in json.load(f)]
    return []

def save_notes(notes):
    with open(DATA_FILE, "w") as f:
        json.dump([n.__dict__ for n in notes], f, indent=4)

def show_menu():
    print("\n=== NoteKeeper ===")
    print("1. Criar nota")
    print("2. Listar notas")
    print("3. Buscar nota por título")
    print("4. Excluir nota")
    print("5. Sair")

def main():
    notes = load_notes()

    while True:
        show_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da nota: ")
            conteudo = input("Conteúdo: ")
            nota = Note(titulo, conteudo)
            notes.append(nota)
            save_notes(notes)
            print("📝 Nota criada com sucesso!")

        elif opcao == "2":
            if not notes:
                print("Nenhuma nota encontrada.")
            else:
                print("\n📒 Suas Notas:")
                for n in notes:
                    print(f"- {n.title} (Criada em {n.created_at})")

        elif opcao == "3":
            termo = input("Digite o título para buscar: ")
            resultado = Note.search(notes, termo)
            if resultado:
                for n in resultado:
                    print(f"\n🔍 {n.title}\n{n.content}\n")
            else:
                print("❌ Nenhuma nota encontrada.")

        elif opcao == "4":
            titulo = input("Título da nota a excluir: ")
            notes = [n for n in notes if n.title != titulo]
            save_notes(notes)
            print("🗑️ Nota excluída com sucesso.")

        elif opcao == "5":
            print("Saindo... até logo!")
            break

if __name__ == "__main__":
    main()
