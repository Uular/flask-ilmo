/**
 * Created by Uula on 2016-03-11.
 */
function showMe (it, box, invert) {
    if (typeof(invert)==='undefined') invert = false;
  var vis = (invert ? !box.checked : box.checked) ? "block" : "none";
  document.getElementById(it).style.display = vis;
}