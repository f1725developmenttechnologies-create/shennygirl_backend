-- Tabla de Clientes
CREATE TABLE IF NOT EXISTS clients (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name TEXT NOT NULL,
    phone TEXT UNIQUE NOT NULL,
    email TEXT,
    birth_date DATE,
    notes TEXT,
    total_visits INT DEFAULT 0,
    total_spent DECIMAL(10,2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Tabla de Servicios
CREATE TABLE IF NOT EXISTS services (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    category TEXT CHECK (category IN ('cabello', 'uñas', 'maquillaje', 'pestañas', 'tatuajes', 'tratamiento')),
    base_price DECIMAL(10,2) NOT NULL,
    estimated_minutes INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Tabla de Citas
CREATE TABLE IF NOT EXISTS appointments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID REFERENCES clients(id) ON DELETE CASCADE,
    service_id UUID REFERENCES services(id) ON DELETE SET NULL,
    scheduled_date DATE NOT NULL,
    scheduled_time TIME NOT NULL,
    status TEXT CHECK (status IN ('scheduled', 'in_progress', 'completed', 'cancelled', 'no_show')) DEFAULT 'scheduled',
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Tabla de Facturas
CREATE TABLE IF NOT EXISTS invoices (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID REFERENCES clients(id) ON DELETE SET NULL,
    appointment_id UUID REFERENCES appointments(id) ON DELETE SET NULL,
    invoice_number SERIAL UNIQUE,
    issue_date DATE DEFAULT CURRENT_DATE,
    subtotal DECIMAL(10,2) NOT NULL,
    tax_rate DECIMAL(5,2) DEFAULT 19.0,
    tax_amount DECIMAL(10,2),
    total_amount DECIMAL(10,2) NOT NULL,
    status TEXT CHECK (status IN ('paid', 'pending', 'overdue')) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Tabla de Items de Factura
CREATE TABLE IF NOT EXISTS invoice_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    invoice_id UUID REFERENCES invoices(id) ON DELETE CASCADE,
    description TEXT NOT NULL,
    quantity INT DEFAULT 1,
    unit_price DECIMAL(10,2) NOT NULL,
    total DECIMAL(10,2) GENERATED ALWAYS AS (quantity * unit_price) STORED
);

-- Tabla de Auditoría (Logs)
CREATE TABLE IF NOT EXISTS audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMP DEFAULT NOW(),
    endpoint TEXT,
    method TEXT,
    ip TEXT,
    user_id UUID REFERENCES clients(id) ON DELETE SET NULL,
    details JSONB
);

-- Insertar servicios de ejemplo (para que la app tenga datos)
INSERT INTO services (id, name, category, base_price, estimated_minutes) VALUES
    (gen_random_uuid(), 'Manicura Básica', 'uñas', 25.00, 30),
    (gen_random_uuid(), 'Uñas Acrílicas', 'uñas', 40.00, 60),
    (gen_random_uuid(), 'Lifting de Pestañas', 'pestañas', 35.00, 45),
    (gen_random_uuid(), 'Maquillaje Social', 'maquillaje', 30.00, 40),
    (gen_random_uuid(), 'Tinte de Raíz', 'cabello', 18.00, 30),
    (gen_random_uuid(), 'Microblading', 'tatuajes', 50.00, 90);

-- Insertar un cliente de ejemplo (opcional)
INSERT INTO clients (id, full_name, phone, email) VALUES
    (gen_random_uuid(), 'María González', '3001234567', 'maria@email.com');