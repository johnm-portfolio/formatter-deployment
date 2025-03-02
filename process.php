<?php
// process.php

// Check if file was uploaded without errors
if(isset($_FILES["upload"]) && $_FILES["upload"]["error"] == 0) {
    $allowed = array("txt" => "text/plain", "md" => "text/markdown");
    $filename = $_FILES["upload"]["name"];
    $filetype = $_FILES["upload"]["type"];
    $filesize = $_FILES["upload"]["size"];

    // Verify file extension
    $ext = pathinfo($filename, PATHINFO_EXTENSION);
    if(!array_key_exists($ext, $allowed)) {
        die("Error: Please select a valid file format.");
    }

    // Verify MIME type of the file
    if(in_array($filetype, $allowed)) {
        // Define a temporary upload location
        $upload_dir = "uploads/";
        if(!is_dir($upload_dir)){
            mkdir($upload_dir, 0777, true);
        }
        $tmp_file = $upload_dir . basename($filename);
        move_uploaded_file($_FILES["upload"]["tmp_name"], $tmp_file);

        // Define an output file path
        $output_file = $upload_dir . "output_" . basename($filename);

        // Run the Python script, passing input and output file paths
        // Ensure your Python script has executable permissions and the correct shebang line
        $command = escapeshellcmd("python format_file.py " . escapeshellarg($tmp_file) . " " . escapeshellarg($output_file));
        $result = shell_exec($command . " 2>&1");  // capture error output
        if (!file_exists($output_file)) {
            die("Error: Output file not found. Debug info: " . $result);
}


        // After processing, force a download of the output file
        if(file_exists($output_file)) {
            header('Content-Description: File Transfer');
            header('Content-Type: application/octet-stream');
            header('Content-Disposition: attachment; filename="'.basename($output_file).'"');
            header('Expires: 0');
            header('Cache-Control: must-revalidate');
            header('Pragma: public');
            header('Content-Length: ' . filesize($output_file));
            flush();
            readfile($output_file);
        
            // Optionally, delete the files after download
            unlink($tmp_file);
            unlink($output_file);
            exit;
        } else {
            die("Error: Output file not found.");
        }
        
    } else {
        die("Error: There was a problem with your file upload.");
    }
} else {
    die("Error: " . $_FILES["upload"]["error"]);
}
?>
