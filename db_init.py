# Criar a estrutura inicial do banco de dados em SQLite

import sqlite3

print(f"Script {__name__} executado.")


def tbl_create():
    """
    Criar as tabelas MEDICOS e PACIENTES.
    """
    con = sqlite3.connect("clinica.db")
    cur = con.cursor()

    cur.execute(
        """
            CREATE TABLE IF NOT EXISTS medicos
            (nome text,
            crm text,
            especialidade text,
            turno text,
            status text) 
        """
    )

    cur.execute(
        """
            CREATE TABLE IF NOT EXISTS pacientes
            (nome text,
            email text,
            telefone text,
            status text) 
        """
    )

    con.commit()
    con.close()

    print("Tabelas criadas.")


def tables_init():
    """Incluir dados iniciais de teste nas tabelas."""

    con = sqlite3.connect("clinica.db")
    cur = con.cursor()


    # cur.execute(
    #     """
    #         INSERT INTO medicos VALUES(
    #             "Rancho Crux",
    #             "0001",
    #             "Traumatologia",
    #             "Noturno",
    #             "Ativo"
    #         )
    #     """
    # )

    medicos = [
        ("Rancho Crux", "0001", "Traumatologia", "Noturno", "Ativo"),
        ("Frederico Evandro", "1111", "Urologia", "Noturno", "Recesso"),
        ("Ernesto Ataronte", "2222", "Oftamologia", "Diurno", "Aposentado"),
    ]

    pacientes = [
        ("Natanael Lima", "natan@gmail.com", "61 9999-0000", "Internado"),
        ("Luciana Lima", "lulu@gmail.com", "61 9999-2222", "Em atendimento"),
    ]

    cur.execute("DELETE FROM medicos")
    cur.execute("DELETE FROM pacientes")

    cur.executemany("INSERT INTO medicos VALUES (?,?,?,?,?)", medicos)
    cur.executemany("INSERT INTO pacientes VALUES (?,?,?,?)", pacientes)
    

    con.commit()
    con.close()

    print("Dados iniciais incluidos nas tabelas.")

if __name__ == "__main__":
    tbl_create()
    tables_init()