//js to initialize the data-table

$(document).ready(function() {
    $('#consoleList').DataTable(
      {
        "pageLength": 2,
        "info": false,
        "lengthChange": false
      });
} );