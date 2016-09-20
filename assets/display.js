

function switch_view(to_id) {
    document.getElementById('dev_pane').style.display="none";
    document.getElementById('des_pane').style.display="none";
    document.getElementById('lead_pane').style.display="none";
    document.getElementById(to_id).style.display="block"

    var name;
    if (to_id == "dev_pane") {
        name = "DEVELOPER";
    } else if (to_id == "des_pane") {
        name = "DESIGNER";
    } else if (to_id == "lead_pane") {
        name = "LEADER";
    }
    document.getElementById('subtitle').innerHTML=name;
    ;
}