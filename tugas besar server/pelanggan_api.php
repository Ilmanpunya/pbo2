<?php
require_once 'database.php';
require_once 'Pelanggan.php';
$db = new MySQLDatabase();
$pelanggan = new Pelanggan($db);
$id=0;
$id_pelanggan=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['id_pelanggan'])){
            $id_pelanggan = $_GET['id_pelanggan'];
        }
        if($id>0){    
            $result = $pelanggan->get_by_id($id);
        }elseif($id_pelanggan>0){
            $result = $pelanggan->get_by_id_pelanggan($id_pelanggan);
        } else {
            $result = $pelanggan->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new pelanggan
        $pelanggan->id_pelanggan = $_POST['id_pelanggan'];
        $pelanggan->nama = $_POST['nama'];
        $pelanggan->umur = $_POST['umur'];
        $pelanggan->waktu = $_POST['waktu'];
       
        $pelanggan->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pelanggan created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pelanggan not created.';
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
        if(isset($_GET['id_pelanggan'])){
            $id_pelanggan = $_GET['id_pelanggan'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $pelanggan->id_pelanggan = $_PUT['id_pelanggan'];
        $pelanggan->nama = $_PUT['nama'];
        $pelanggan->umur = $_PUT['umur'];
        $pelanggan->waktu = $_PUT['waktu'];
        if($id>0){    
            $pelanggan->update($id);
        }elseif($id_pelanggan<>""){
            $pelanggan->update_by_id_pelanggan($id_pelanggan);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pelanggan updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pelanggan update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['id_pelanggan'])){
            $id_pelanggan = $_GET['id_pelanggan'];
        }
        if($id>0){    
            $pelanggan->delete($id);
        }elseif($id_pelanggan>0){
            $pelanggan->delete_by_id_pelanggan($id_pelanggan);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pelanggan deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pelanggan delete failed.';
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