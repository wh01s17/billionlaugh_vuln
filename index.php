<?php
// Permitir acceso desde cualquier host (solo para prueba local)
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Leer raw body XML input
    $rawBody = file_get_contents('php://input');
    // Desactiva posibles protecciones si están activas
    libxml_disable_entity_loader(false); 
    
    $dom = new DOMDocument();
    // CARGA ENTIDADES EXTERNAS POR DEFECTO
    $dom->loadXML($rawBody, LIBXML_NOENT | LIBXML_DTDLOAD);
    
    echo json_encode([
        "message" => "Procesado",
        "output" => $dom->saveXML()
    ]);
} else {
    echo json_encode(["message" => "Usa POST con cuerpo XML"]);
}
?>

