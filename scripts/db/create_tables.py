import psycopg2
from collector.core.settings import DB_NAME, HOST, PASSWORD, PORT, USER


CONNECT_DB = f"host={HOST} port={PORT} dbname={DB_NAME} user={USER} password={PASSWORD}"


def execute_query(sql_query: str):
    conn, cur = None, None
    try:
        # Make a connection to db
        conn = psycopg2.connect(CONNECT_DB)

        # Create cursor
        cur = conn.cursor()

        # Send sql to request
        cur.execute(sql_query)

        # Committing
        conn.commit()
    except (Exception, psycopg2.Error) as error:  # pylint: disable=broad-except
        print("Error connecting to postgreSQL", error)
    finally:
        if conn:
            cur.close()  # type: ignore
            conn.close()
            print("PostgreSQL connection is closed")


create_table_query = """
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TABLE users(
    user_id uuid DEFAULT uuid_generate_v4 (),
    username VARCHAR,
    first_name VARCHAR,
    last_name VARCHAR,
    portfolio_url VARCHAR,
    bio VARCHAR,
    full_name VARCHAR,
    instagram_username VARCHAR,
    twitter_username VARCHAR,
    total_likes INTEGER,
    total_photos INTEGER,
    for_hire BOOLEAN,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (user_id)
);

CREATE TABLE photos(
    photo_id uuid DEFAULT uuid_generate_v4 (),
    title VARCHAR,
    description VARCHAR,
    likes INTEGER,
    tags TEXT [],
    categoris TEXT [],
    published_at DATE,
    stock_type VARCHAR,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (photo_id)
);

CREATE TABLE user_images(
    image_id uuid DEFAULT uuid_generate_v4 (),
    raw VARCHAR,
    small VARCHAR,
    regular VARCHAR,
    large VARCHAR,
    user_id uuid,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (image_id)
);

CREATE TABLE photo_images(
    image_id uuid DEFAULT uuid_generate_v4 (),
    raw VARCHAR,
    small VARCHAR,
    regular VARCHAR,
    large VARCHAR,
    photo_id uuid,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (image_id)
);

CREATE TRIGGER set_timestamp_to_user_images
BEFORE UPDATE ON user_images
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

CREATE TRIGGER set_timestamp_to_photo_images
BEFORE UPDATE ON photo_images
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

CREATE TRIGGER set_timestamp_to_users
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

CREATE TRIGGER set_timestamp_to_photos
BEFORE UPDATE ON photos
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

ALTER TABLE user_images
ADD CONSTRAINT fk_user
FOREIGN KEY (user_id)
REFERENCES users(user_id)
ON DELETE CASCADE;

ALTER TABLE photo_images
ADD CONSTRAINT fk_photo
FOREIGN KEY (photo_id)
REFERENCES photos(photo_id)
ON DELETE CASCADE;
 """

if __name__ == "__main__":
    execute_query(create_table_query)
