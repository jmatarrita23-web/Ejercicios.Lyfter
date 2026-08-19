# Normalización de tablas

## 1. Tabla original (UNF)

| Order ID | Customer Name | Customer Phone | Address | Item ID | Item Name | Price | Quantity | Special Request | Delivery Time |
|---|---|---|---|---|---|---|---|---|---|
| 001 | Alice | 123-456-7890 | 123 Main St | 101 | Cheeseburger | $8 | 2 | No onions | 6:00 PM |
| 001 | Alice | 123-456-7890 | 123 Main St | 102 | Fries | $3 | 1 | Extra ketchup | 6:00 PM |
| 002 | Bob | 987-654-3210 | 456 Elm St | 103 | Pizza | $12 | 1 | Extra cheese | 7:30 PM |
| 002 | Bob | 987-654-3210 | 4th Avenue | 102 | Fries | $3 | 2 | None | 7:30 PM |
| 003 | Claire | 555-123-4567 | 789 Oak St | 105 | Salad | $6 | 1 | No croutons | 12:00 PM |
| 004 | Claire | 555-123-4567 | 464 Georgia St | 106 | Water | $1 | 1 | None | 5:00 PM |

---

# 2. Primera Forma Normal (1FN)

### Clave primaria

**(Order ID, Item ID)**

| Order ID (PK) | Item ID (PK) | Customer Name | Customer Phone | Address | Item Name | Price | Quantity | Special Request | Delivery Time |
|---|---|---|---|---|---|---|---|---|---|
| 001 | 101 | Alice | 123-456-7890 | 123 Main St | Cheeseburger | $8 | 2 | No onions | 6:00 PM |
| 001 | 102 | Alice | 123-456-7890 | 123 Main St | Fries | $3 | 1 | Extra ketchup | 6:00 PM |
| 002 | 103 | Bob | 987-654-3210 | 456 Elm St | Pizza | $12 | 1 | Extra cheese | 7:30 PM |
| 002 | 102 | Bob | 987-654-3210 | 4th Avenue | Fries | $3 | 2 | None | 7:30 PM |
| 003 | 105 | Claire | 555-123-4567 | 789 Oak St | Salad | $6 | 1 | No croutons | 12:00 PM |
| 004 | 106 | Claire | 555-123-4567 | 464 Georgia St | Water | $1 | 1 | None | 5:00 PM |

---

# 3. Segunda Forma Normal (2FN)

## Tabla ORDER

| Order ID (PK) | Customer Name | Customer Phone | Address | Delivery Time |
|---|---|---|---|---|
| 001 | Alice | 123-456-7890 | 123 Main St | 6:00 PM |
| 002 | Bob | 987-654-3210 | 456 Elm St | 7:30 PM |
| 003 | Claire | 555-123-4567 | 789 Oak St | 12:00 PM |
| 004 | Claire | 555-123-4567 | 464 Georgia St | 5:00 PM |

## Tabla ITEM

| Item ID (PK) | Item Name | Price |
|---|---|---|
| 101 | Cheeseburger | $8 |
| 102 | Fries | $3 |
| 103 | Pizza | $12 |
| 105 | Salad | $6 |
| 106 | Water | $1 |

## Tabla ORDER_ITEM

| Order ID (PK, FK) | Item ID (PK, FK) | Quantity | Special Request |
|---|---|---|---|
| 001 | 101 | 2 | No onions |
| 001 | 102 | 1 | Extra ketchup |
| 002 | 103 | 1 | Extra cheese |
| 002 | 102 | 2 | None |
| 003 | 105 | 1 | No croutons |
| 004 | 106 | 1 | None |

---

# 4. Tercera Forma Normal (3FN)

## Tabla CUSTOMER

| Customer Phone (PK) | Customer Name |
|---|---|
| 123-456-7890 | Alice |
| 987-654-3210 | Bob |
| 555-123-4567 | Claire |

## Tabla ORDER

| Order ID (PK) | Customer Phone (FK) | Address | Delivery Time |
|---|---|---|---|
| 001 | 123-456-7890 | 123 Main St | 6:00 PM |
| 002 | 987-654-3210 | 456 Elm St | 7:30 PM |
| 003 | 555-123-4567 | 789 Oak St | 12:00 PM |
| 004 | 555-123-4567 | 464 Georgia St | 5:00 PM |

## Tabla ITEM

| Item ID (PK) | Item Name | Price |
|---|---|---|
| 101 | Cheeseburger | $8 |
| 102 | Fries | $3 |
| 103 | Pizza | $12 |
| 105 | Salad | $6 |
| 106 | Water | $1 |

## Tabla ORDER_ITEM

| Order ID (PK, FK) | Item ID (PK, FK) | Quantity | Special Request |
|---|---|---|---|
| 001 | 101 | 2 | No onions |
| 001 | 102 | 1 | Extra ketchup |
| 002 | 103 | 1 | Extra cheese |
| 002 | 102 | 2 | None |
| 003 | 105 | 1 | No croutons |
| 004 | 106 | 1 | None |

---










# Normalización de tablas parte 2

## 1. Tabla original (UNF)

| VIN | Make | Model | Year | Color | Owner ID | Owner Name | Owner Phone | Insurance Company | Insurance Policy |
|---|---|---|---|---|---|---|---|---|---|
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 101 | Alice | 123-456-7890 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 102 | Bob | 987-654-3210 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue | 103 | Claire | 555-123-4567 | DEF Insurance | Collision |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red | 104 | Dave | 111-222-3333 | GHI Insurance | Basic Legal |

---

# 2. Primera Forma Normal (1FN)

### Clave primaria

**(VIN, Owner ID)**

| VIN (PK) | Owner ID (PK) | Make | Model | Year | Color | Owner Name | Owner Phone | Insurance Company | Insurance Policy |
|---|---|---|---|---|---|---|---|---|---|
| 1HGCM82633A | 101 | Honda | Accord | 2003 | Silver | Alice | 123-456-7890 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | 102 | Honda | Accord | 2003 | Silver | Bob | 987-654-3210 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | 103 | Honda | CR-V | 2014 | Blue | Claire | 555-123-4567 | DEF Insurance | Collision |
| 1G1RA6EH1FU | 104 | Chevrolet | Volt | 2015 | Red | Dave | 111-222-3333 | GHI Insurance | Basic Legal |

---

# 3. Segunda Forma Normal (2FN)

## Tabla VEHICLE

| VIN (PK) | Make | Model | Year | Color |
|---|---|---|---|---|
| 1HGCM82633A | Honda | Accord | 2003 | Silver |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red |

## Tabla OWNER

| Owner ID (PK) | Owner Name | Owner Phone |
|---|---|---|
| 101 | Alice | 123-456-7890 |
| 102 | Bob | 987-654-3210 |
| 103 | Claire | 555-123-4567 |
| 104 | Dave | 111-222-3333 |

## Tabla VEHICLE_OWNER

| VIN (PK, FK) | Owner ID (PK, FK) | Insurance Company | Insurance Policy |
|---|---|---|---|
| 1HGCM82633A | 101 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | 102 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | 103 | DEF Insurance | Collision |
| 1G1RA6EH1FU | 104 | GHI Insurance | Basic Legal |

---

# 4. Tercera Forma Normal (3FN)

## Tabla VEHICLE

| VIN (PK) | Make | Model | Year | Color |
|---|---|---|---|---|
| 1HGCM82633A | Honda | Accord | 2003 | Silver |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red |

## Tabla OWNER

| Owner ID (PK) | Owner Name | Owner Phone |
|---|---|---|
| 101 | Alice | 123-456-7890 |
| 102 | Bob | 987-654-3210 |
| 103 | Claire | 555-123-4567 |
| 104 | Dave | 111-222-3333 |

## Tabla INSURANCE

| Insurance Company (PK) | Insurance Policy |
|---|---|
| ABC Insurance | Fire & Theft |
| XYZ Insurance | Full Cover |
| DEF Insurance | Collision |
| GHI Insurance | Basic Legal |

## Tabla VEHICLE_OWNER

| VIN (PK, FK) | Owner ID (PK, FK) | Insurance Company (FK) |
|---|---|---|
| 1HGCM82633A | 101 | ABC Insurance |
| 1HGCM82633A | 102 | XYZ Insurance |
| 5J6RM4H79EL | 103 | DEF Insurance |
| 1G1RA6EH1FU | 104 | GHI Insurance |

---

# 5. Resultado final

### VEHICLE
- VIN (PK)
- Make
- Model
- Year
- Color

### OWNER
- Owner ID (PK)
- Owner Name
- Owner Phone

### INSURANCE
- Insurance Company (PK)
- Insurance Policy

### VEHICLE_OWNER
- VIN (PK, FK)
- Owner ID (PK, FK)
- Insurance Company (FK)

