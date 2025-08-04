CREATE DATABASE ClinicaSaludTotal;
USE ClinicaSaludTotal;

CREATE TABLE Pacientes (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Edad INT,
    Genero VARCHAR(10),
    HistorialMedico TEXT,
    Contacto VARCHAR(100)
);

INSERT INTO Pacientes (Nombre, Edad, Genero, HistorialMedico, Contacto) VALUES
('Juan Perez', 35, 'Masculino', 'Hipertensión', 'juan@example.com'),
('María López', 45, 'Femenino', 'Diabetes', 'maria@example.com'),
('Pedro García', 28, 'Masculino', 'Asma', 'pedro@example.com');
