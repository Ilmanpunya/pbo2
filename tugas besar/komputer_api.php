<?php
require_once 'database.php';
require_once 'Komputer.php';
$db = new MySQLDatabase();
$komputer = new Komputer($db);
$id=0;
$id_komputer=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['id_komputer'])){
            $id_komputer = $_GET['id_komputer'];
        }
        if($id>0){    
            $result = $komputer->get_by_id($id);
        }elseif($id_komputer>0){
            $result = $komputer->get_by_id_komputer($id_komputer);
        } else {
            $result = $komputer->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new komputer
        $komputer->id_komputer = $_POST['id_komputer'];
        $komputer->Billing = $_POST['Billing'];
        $komputer->Jenis = $_POST['Jenis'];
        $komputer->Status = $_POST['Status'];
       
        $komputer->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Komputer created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Komputer not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['id_komputer'])){
            $id_komputer = $_GET['id_komputer'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $komputer->id_komputer = $_PUT['id_komputer'];
        $komputer->Billing = $_PUT['Billing'];
        $komputer->Jenis = $_PUT['Jenis'];
        $komputer->Status = $_PUT['Status'];
        if($id>0){    
            $komputer->update($id);
        }elseif($id_komputer<>""){
            $komputer->update_by_id_komputer($id_komputer);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Komputer updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Komputer update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['id_komputer'])){
            $id_komputer = $_GET['id_komputer'];
        }
        if($id>0){    
            $komputer->delete($id);
        }elseif($id_komputer>0){
            $komputer->delete_by_id_komputer($id_komputer);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Komputer deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Komputer delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>