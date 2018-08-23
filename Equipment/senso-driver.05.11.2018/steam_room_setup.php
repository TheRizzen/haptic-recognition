<?php
 $fname_lh = "lighthousedb.json";
 $fname_rm = "chaperone_info.vrchap";
 $fname_out = "lh_data.ini";

 include "fm.php";

 @$f  = file_get_contents($fname_lh);
 if(!$f){
  die ("can't find lighthouse db file at path $fname_lh\n");
 }

 @$f1 = file_get_contents($fname_rm);
 if(!$f1){
  die ("can't find room setup file at path $fname_rm\n");
 }

 echo "LH + room setup files found, parsing..\n";

 $o = json_decode($f,TRUE);
 $bases = array();
 foreach($o['base_stations'] as $name => $value){
   $serial = $value['config']['serialNumber'];
   $bases[$serial] = $value['dynamic_states']; 
 }

 $universes = array();
 foreach($o['known_universes'] as $u){
  $id = $u['id'];	
  $universes[$id]['tilt'] = $u['tilt'];
  $universes[$id]['bases'] = $u['base_stations'];
 }

 $o = json_decode($f1,TRUE);

 $universe = array();
 $ft=0;
 foreach($o['universes'] as $u){
  $ts = strtotime($u['time']);	
  if($ts>$ft){ $universe = $u;$ft = $ts; }
 }

 $id = $universe["universeID"];
 $res_u = array();

 $res_u["translation"] = $universe['standing']["translation"];
 $res_u["pitch"] = $universes[$id]['tilt']['pitch'];
 $res_u["roll"] = $universes[$id]['tilt']['roll'];
 $res_u["yaw"] = $universe['standing']['yaw'];
 $res_u["id"] = $id;
 $res_u["ts"] = $ft;

 $vt = $res_u['translation'];
 $vt = array(-1000*$vt[0],1000*$vt[2],-1000*$vt[1]);
 $vt = Rotate_Vector_Raw($vt,Rotate_Quat(array(0,0,-$res_u['yaw']),array(1,0,0,0)));

 $bs = $universes[$id]['bases'];
 $lh = array();
 foreach($bs as $bts){
  $id = $bts['base_serial_number'];
  $did = $bts['target_pose']['dynamic_state_id'];
  $pose = $bts['target_pose']['pose'];
  $bss = $bases[$id][$did];
  $bs_mode = $bss['dynamic_state']['basestation_mode'];
  $tilt = $bss['tilt'];
  $ts = $bss['time_last_seen'];
  $b = array('id'=>$id,'pose'=>$pose,'mode'=>$bs_mode,'tilt'=>$tilt,'ts'=>$ts);
  $pos = array(-1000*$pose[4],1000*$pose[6],-1000*$pose[5]);
  $quat = array($pose[3],-$pose[0],$pose[2],-$pose[1]);
//  $pos = Rotate_Vector_Raw($pos,$quat);
  $quat = Rotate_Quat(array(0,$res_u['roll'],0),$quat);
  $quat = Rotate_Quat(array(-$res_u['pitch'],0,0),$quat);
  $quat = Rotate_Quat(array(0,0,-$res_u['yaw']),$quat);
  $pos = Rotate_Vector_Raw($pos,$quat);
  $b['p']=array($pos[0] - $vt[0], $pos[1] - $vt[1], $pos[2] - $vt[2]);
  $b['q']=$quat;
  if(!isset($lh[$bs_mode]) || $lh[$bs_mode]['ts']<$ts)$lh[$bs_mode] = $b;
 }

// print_r($vt); 
// print_r($res_u);

 ksort($lh);
 @$f = fopen($fname_out,"w");
 if(!$f){
  die("can't open output file $fname_out for writing\n");
 }

 foreach($lh as $cam){
  $s=sprintf("%d %f %f %f %f %f %f %f\n",$cam['mode'],$cam['p'][0],$cam['p'][1],$cam['p'][2],$cam['q'][0],$cam['q'][1],$cam['q'][2],$cam['q'][3]);
  fputs($f,$s);
  echo "BS $s";
 }
 fclose($f);

 echo "File $fname_out is ready to use with senso_ui\n";

?>
