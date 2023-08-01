<?php
//Simpanlah dengan nama file : Komputer.php
require_once 'database.php';
class Komputer 
{
    private $db;
    private $table = 'komputer';
    public $id_komputer = "";
    public $Billing = "";
    public $Jenis = "";
    public $Status = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_id_komputer(int $id_komputer)
    {
        $query = "SELECT * FROM $this->table WHERE id_komputer = $id_komputer";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`id_komputer`,`Billing`,`Jenis`,`Status`) VALUES ('$this->id_komputer','$this->Billing','$this->Jenis','$this->Status')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET id_komputer = '$this->id_komputer', Billing = '$this->Billing', Jenis = '$this->Jenis', Status = '$this->Status' 
        WHERE ID = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_id_komputer($id_komputer): int
    {
        $query = "UPDATE $this->table SET id_komputer = '$this->id_komputer', Billing = '$this->Billing', Jenis = '$this->Jenis', Status = '$this->Status' 
        WHERE id_komputer = $id_komputer";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE ID = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_id_komputer($id_komputer): int
    {
        $query = "DELETE FROM $this->table WHERE id_komputer = $id_komputer";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>