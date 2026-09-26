def connexion_db():
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        'mysql+pymysql://GERWIN:Gerwin1234%40@localhost/gestion')
    session_factory = sessionmaker(bind=engine)
    session = session_factory()

    try:
        session.execute(text("SELECT 1"))
        print("connectée")
        return session_factory
    except Exception as e:
        print("connexion echouée ", e)
        return None
    finally:
        session.close()
