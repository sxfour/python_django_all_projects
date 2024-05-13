CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

ALTER TABLE public."PostgreSQLViewer_users" 
  ADD COLUMN created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(), 
  ADD COLUMN updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(), 
  ADD COLUMN completed_at TIMESTAMPTZ;

CREATE TRIGGER set_timestamp
BEFORE UPDATE ON public."PostgreSQLViewer_users"
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();