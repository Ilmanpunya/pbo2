<?php
require_once 'database.php';
require_once 'Transaksi.php';
$db = new MySQLDatabase();
$transaksi = new Transaksi($db);
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
            $result = $transaksi->get_by_id($id);
        }elseif($id_pelanggan>0){
            $result = $transaksi->get_by_id_pelanggan($id_pelanggan);
        } else {
            $result = $transaksi->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new transaksi
        $transaksi->id_pelanggan = $_POST['id_pelanggan'];
        $transaksi->Billing = $_POST['Billing'];
        $transaksi->waktu = $_POST['waktu'];
       
        $transaksi->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Transaksi created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Transaksi not created.';
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
        $transaksi->id_pelanggan = $_PUT['id_pelanggan'];
        $transaksi->Billing = $_PUT['Billing'];
        $transaksi->waktu = $_PUT['waktu'];
        if($id>0){    
            $transaksi->update($id);
        }elseif($id_pelanggan<>""){
            $transaksi->update_by_id_pelanggan($id_pelanggan);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Transaksi updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Transaksi update failed.';
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
            $transaksi->delete($id);
        }elseif($id_pelanggan>0){
            $transaksi->delete_by_id_pelanggan($id_pelanggan);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Transaksi deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Transaksi delete failed.';
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