$(document).ready(function() {
    $('#example').DataTable({
        "paging": true, // false to disable pagination (or any other option)
        "pagingType": "simple_numbers",
        "searching": false,
        // 'deferRender': true,
    });
    $('.dataTables_length').addClass('bs-select');
} );