-- Crear tabla de servidores
CREATE TABLE IF NOT EXISTS servers (
    server_id BIGINT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    owner_id BIGINT,
    created_at DATETIME,
    description TEXT,
    member_count INT DEFAULT 0,
    total_roles INT DEFAULT 0,
    total_channels INT DEFAULT 0,
    afk_timeout INT,
    afk_channel_id BIGINT,
    system_channel_id BIGINT,
    icon_url TEXT,
    features TEXT
);

-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT PRIMARY KEY,
    server_id BIGINT,
    username VARCHAR(255),
    display_name VARCHAR(255),
    is_bot BOOLEAN,
    joined_at DATETIME,
    status VARCHAR(50),
    avatar_url TEXT,
    boosting_since DATETIME,
    warning_count INT DEFAULT 0,
    FOREIGN KEY (server_id) REFERENCES servers (server_id) ON DELETE CASCADE
);

-- Crear tabla de roles
CREATE TABLE IF NOT EXISTS roles (
    role_id BIGINT PRIMARY KEY,
    server_id BIGINT,
    name VARCHAR(255),
    color TEXT, -- Color del rol en formato hexadecimal
    position INT,
    mentionable BOOLEAN, -- Indica si el rol es mencionable
    hoist BOOLEAN, -- Indica si el rol es "hoisted" (destacado)
    permissions BOOLEAN, -- Permisos del rol en formato bitfield

    FOREIGN KEY (server_id) REFERENCES servers (server_id) ON DELETE CASCADE
);

-- Crear tabla de relación muchos-a-muchos: usuarios y roles
CREATE TABLE IF NOT EXISTS user_roles (
    user_id BIGINT,
    role_id BIGINT,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles (role_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS warnings (
    warning_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT,
    server_id BIGINT,
    reason TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
    FOREIGN KEY (server_id) REFERENCES servers (server_id) ON DELETE CASCADE
);