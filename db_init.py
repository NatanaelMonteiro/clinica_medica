# Criar a estrutura inicial do banco de dados em SQLite

import connection

print(f"Script {__name__} executado.")


def tbl_create():
    """
    Criar as tabelas MEDICOS e PACIENTES.
    """
    con, cur = connection.get()

    try:
        cur.execute("DROP TABLE medicos")
        cur.execute("DROP TABLE pacientes")
    except:
        pass


    cur.execute(
        """
            CREATE TABLE IF NOT EXISTS medicos
            (id integer PRIMARY KEY AUTOINCREMENT,
            nome text,
            crm text,
            especialidade text,
            turno text,
            status text) 
        """
    )

    cur.execute(
        """
            CREATE TABLE IF NOT EXISTS pacientes
            (id integer PRIMARY KEY AUTOINCREMENT,
            nome text,
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

    con, cur = connection.get()



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
        ("Evaristo Neves", "3333", "Psicologia", "Diurno", "Ativo"),
        ("Garibaldo Nunes", "4444", "Cardiologia", "Noturno", "Recesso"),
    ]

    pacientes = [
        ("Natanael Lima", "natan@gmail.com", "61 9999-0000", "Internado"),
        ("Luciana Lima", "lulu@gmail.com", "61 9999-2222", "Em atendimento"),
        ("Luciete Lima", "mariazinha@gmail.com", "61 9999-1111", "Em tratamento"),
        ("Izaias Lima", "izaias@gmail.com", "61 9999-3333", "Liberado"),
    ]

    cur.execute("DELETE FROM medicos")
    cur.execute("DELETE FROM pacientes")

    if connection.DB_TYPE == "psql":
        cur.executemany("INSERT INTO medicos VALUES (DEFAULT,%s,%s,%s,%s,%s)", medicos)
        cur.executemany("INSERT INTO pacientes VALUES (DEFAULT,%s,%s,%s,%s)", pacientes)
    else:
        cur.executemany("INSERT INTO medicos VALUES (NULL,?,?,?,?,?)", medicos)
        cur.executemany("INSERT INTO pacientes VALUES (NULL,?,?,?,?)", pacientes)
    

    con.commit()
    con.close()

    print("Dados iniciais incluidos nas tabelas.")

if __name__ == "__main__":
    tbl_create()
    tables_init()
