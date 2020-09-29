$(document).ready(function() {
    var listCount = 1;

    $(document).on('click','#data_style',  function() {
        listCount = 1;
        $('#form-container').html('');
        $('#form-buttons').html('');

        if ($('#data_style').val() == 'List') {
            var listForm = `
                <label>Item ${listCount}</label>
                <input name="item-${listCount}" class="form-control">
                `;

            $('#form-container').html(listForm);
            $('#form-buttons').html('<div class="btn btn-warning container-fluid mt-3" id="add-item">Add</div>');
        } else if ($('#data_style').val() == 'Definition') {
            var dataForm = `
                <label>Definition</label>
                <input name="definition" class="form-control">
                `;

            $('#form-container').html(dataForm);
        } 

    });
    $(document).on('click', '#add-item',function() {
        listCount++
        var itemInput = `
        <label>Item ${listCount}</label>
        <input name="item-${listCount}" class="form-control">
        `
        $('#form-container').append(itemInput);
    });
});