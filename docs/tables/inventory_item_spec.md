# Inventory Item Table Specification

## Table Details
- **Table Name**: `u_inventory_item`
- **Table Label**: Inventory Item
- **Extends**: Base Table
- **Auto Number**: Yes (format: INV0001000)

## Field Specifications

### Item Information
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| item_name | String | 100 | Yes | - |
| item_code | String | 50 | Yes | - |
| item_category | Choice | - | Yes | Medication, Medical Supplies, Surgical Instruments, Laboratory Supplies, Food/Treats, Cleaning Supplies, Office Supplies |
| item_subcategory | Choice | - | No | Antibiotics, Pain Management, Vaccines, Bandages, Syringes, Gloves, Test Kits, Dog Food, Cat Food, Disinfectant |
| description | String | 500 | No | - |
| manufacturer | String | 100 | No | - |
| brand | String | 100 | No | - |
| model_number | String | 50 | No | - |

### Inventory Tracking
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| current_stock | Integer | - | Yes | - |
| minimum_stock | Integer | - | Yes | - |
| maximum_stock | Integer | - | No | - |
| reorder_point | Integer | - | Yes | - |
| reorder_quantity | Integer | - | No | - |
| unit_of_measure | Choice | - | Yes | Each, Box, Bottle, Vial, Package, Case, Pound, Kilogram, Liter, Milliliter |
| storage_location | Choice | - | No | Pharmacy, Supply Room A, Supply Room B, Refrigerated Storage, Freezer, Surgery Suite, Laboratory |

### Pricing Information
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| unit_cost | Currency | - | No | - |
| selling_price | Currency | - | No | - |
| supplier | String | 100 | No | - |
| supplier_contact | String | 100 | No | - |
| last_order_date | Date | - | No | - |
| last_order_quantity | Integer | - | No | - |
| next_order_due | Date | - | No | - |

### Medication-Specific Fields
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| is_medication | Boolean | - | No | - |
| requires_prescription | Boolean | - | No | - |
| controlled_substance | Boolean | - | No | - |
| dea_schedule | Choice | - | No | Schedule I, Schedule II, Schedule III, Schedule IV, Schedule V, Not Controlled |
| dosage_form | Choice | - | No | Tablet, Capsule, Liquid, Injection, Topical, Drops, Spray |
| strength | String | 50 | No | - |
| expiration_tracking | Boolean | - | No | - |

### Quality Control
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| lot_number | String | 50 | No | - |
| expiration_date | Date | - | No | - |
| temperature_requirements | Choice | - | No | Room Temperature, Refrigerated, Frozen, Temperature Controlled |
| special_handling | String | 200 | No | - |
| disposal_requirements | String | 200 | No | - |

### Status Fields
| Field Name | Type | Length | Mandatory | Choice Options |
|------------|------|--------|-----------|----------------|
| item_status | Choice | - | Yes | Active, Inactive, Discontinued, Backordered, Expired |
| stock_status | Choice | - | Yes | In Stock, Low Stock, Out of Stock, Overstocked |
| last_updated | Date/Time | - | No | - |
| updated_by | Reference | - | No | sys_user |

## Business Rules
1. **Auto-set Stock Status**: Based on current_stock vs minimum/maximum levels
2. **Reorder Alerts**: Generate alerts when current_stock <= reorder_point
3. **Expiration Monitoring**: Alert for items expiring within 30 days
4. **Usage Tracking**: Decrement stock when items are used in treatments
5. **Controlled Substance Logging**: Enhanced tracking for DEA controlled substances

## Form Layout
1. **Item Details**: item_name, item_code, item_category, item_subcategory, description
2. **Manufacturer Info**: manufacturer, brand, model_number
3. **Inventory Levels**: current_stock, minimum_stock, maximum_stock, reorder_point, reorder_quantity
4. **Storage & Units**: unit_of_measure, storage_location, temperature_requirements
5. **Pricing**: unit_cost, selling_price, supplier, supplier_contact
6. **Medication Info**: is_medication, requires_prescription, controlled_substance, dea_schedule, dosage_form, strength
7. **Quality Control**: lot_number, expiration_date, special_handling, disposal_requirements
8. **Status**: item_status, stock_status, last_updated, updated_by

## Related Lists
- **Stock Movements**: Track all inventory in/out transactions
- **Usage History**: Items used in treatments and procedures
- **Purchase Orders**: Ordering history and pending orders
