<?php
//Simpanlah dengan nama file : Pelanggan.php
require_once 'database.php';
class Pelanggan 
{
    private $db;
    private $table = 'pelanggan';
    public $id_pelanggan = "";
    public $nama = "";
    public $umur = "";
    public $waktu = "";
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
    public function get_by_id_pelanggan(int $id_pelanggan)
    {
        $query = "SELECT * FROM $this->table WHERE id_pelanggan = $id_pelanggan";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`id_pelanggan`,`nama`,`umur`,`waktu`) VALUES ('$this->id_pelanggan','$this->nama','$this->umur','$this->waktu')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET id_pelanggan = '$this->id_pelanggan', nama = '$this->nama', umur = '$this->umur', waktu = '$this->waktu' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_id_pelanggan($id_pelanggan): int
    {
        $query = "UPDATE $this->table SET id_pelanggan = '$this->id_pelanggan', nama = '$this->nama', umur = '$this->umur', waktu = '$this->waktu' 
        WHERE id_pelanggan = $id_pelanggan";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_id_pelanggan($id_pelanggan): int
    {
        $query = "DELETE FROM $this->table WHERE id_pelanggan = $id_pelanggan";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>