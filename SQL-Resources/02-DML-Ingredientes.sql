INSERT INTO `heladeria`.`ingredientes` (`id`, `nombre`, `precio`, `calorias`, `vegetariano`, `inventario`, `tipo`, `sabor`) VALUES (1, 'Helado de fresa', 1500, 50.0, False, 1.0, 'Base', 'Fresa');
INSERT INTO `heladeria`.`ingredientes` (`id`, `nombre`, `precio`, `calorias`, `vegetariano`, `inventario`, `tipo`, `sabor`) VALUES (2, 'Chispas de chocolate', 2500, 80.0, False, .8, 'Base', 'Chocolate');
INSERT INTO `heladeria`.`ingredientes` (`id`, `nombre`, `precio`, `calorias`, `vegetariano`, `inventario`, `tipo`, `sabor`) VALUES (3, 'Maní sin dulce', 1200, 10.0, True, 20.0, 'Base', 'Maní');
INSERT INTO `heladeria`.`ingredientes` (`id`, `nombre`, `precio`, `calorias`, `vegetariano`, `inventario`, `tipo`, `sabor`) VALUES (4, 'Helado de vainilla', 1300, 48, False, .2, 'Base', 'Vainilla');
INSERT INTO `heladeria`.`ingredientes` (`id`, `nombre`, `precio`, `calorias`, `vegetariano`, `inventario`, `tipo`, `sabor`) VALUES (5, 'Helado de chocolate', 1800, 120.0, False, .6, 'Base', 'Chocolate');
INSERT INTO `heladeria`.`ingredientes` (`id`, `nombre`, `precio`, `calorias`, `vegetariano`, `inventario`, `tipo`, `sabor`) VALUES (6, 'Cereales', 500, 10.0, True, 1.2, 'Base', 'Maíz');
INSERT INTO `heladeria`.`ingredientes` (`id`, `nombre`, `precio`, `calorias`, `vegetariano`, `inventario`, `tipo`, `sabor`) VALUES (7, 'Frutas varias', 900, '25.0', True, 5.0, 'Complemento', 'Frutas varias');
INSERT INTO `heladeria`.`ingredientes` (`id`, `nombre`, `precio`, `calorias`, `vegetariano`, `inventario`, `tipo`, `sabor`) VALUES (8, 'Chispas de colores', 1000, 52.0, True, 5.0, 'Complemento', 'Dulce');
INSERT INTO `heladeria`.`ingredientes` (`id`, `nombre`, `precio`, `calorias`, `vegetariano`, `inventario`, `tipo`, `sabor`) VALUES (9, 'Crema de leche', 1500, 400.0, False, 10.0, 'Complemento', 'Leche');
INSERT INTO `heladeria`.`ingredientes` (`id`, `nombre`, `precio`, `calorias`, `vegetariano`, `inventario`, `tipo`, `sabor`) VALUES (10, 'Crema chantilly', 3000, 200.0, False, 5.0, 'Complemento', 'Crema');

INSERT INTO `heladeria`.`productos` (`id`, `nombre`, `precio`, `ventas_dia`, `precio_ventas_dia`, `id_ingrediente1`, `id_ingrediente2`, `id_ingrediente3`, `tipo`) VALUES ('1', 'Copa Mickey de fresa', 15000, 0, 0, 1, 2, 3, 'Copa');
INSERT INTO `heladeria`.`productos` (`id`, `nombre`, `precio`, `ventas_dia`, `precio_ventas_dia`, `id_ingrediente1`, `id_ingrediente2`, `id_ingrediente3`, `tipo`) VALUES ('2', 'Copa Donald', 12000, 0, 0, 6, 9, 8, 'Copa');
INSERT INTO `heladeria`.`productos` (`id`, `nombre`, `precio`, `ventas_dia`, `precio_ventas_dia`, `id_ingrediente1`, `id_ingrediente2`, `id_ingrediente3`, `tipo`) VALUES ('3', 'Copa Goofy', 11500, 0, 0, 4, 9, 7, 'Copa');
INSERT INTO `heladeria`.`productos` (`id`, `nombre`, `precio`, `ventas_dia`, `precio_ventas_dia`, `id_ingrediente1`, `id_ingrediente2`, `id_ingrediente3`, `tipo`) VALUES ('4', 'Malteada Deisy', 18000, 0, 0, 4, 9, 7, 'Malteada');
INSERT INTO `heladeria`.`productos` (`id`, `nombre`, `precio`, `ventas_dia`, `precio_ventas_dia`, `id_ingrediente1`, `id_ingrediente2`, `id_ingrediente3`, `tipo`) VALUES ('5', 'Malteada Pluto', 15000, 0, 0, 5, 9, 8, 'Malteada');
INSERT INTO `heladeria`.`productos` (`id`, `nombre`, `precio`, `ventas_dia`, `precio_ventas_dia`, `id_ingrediente1`, `id_ingrediente2`, `id_ingrediente3`, `tipo`) VALUES ('6', 'Malteada Minnie', 12000, 0, 0, 1, 9, 8, 'Malteada');
