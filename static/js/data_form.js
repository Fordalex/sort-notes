$(document).ready(function() {
    var listCount = 1;

    $(document).on('click','#data_style',  function() {
        listCount = 1;
        $('#form-container').html('');
        $('#form-buttons').html('');

        if ($('#data_style').val() == 'List') {
            var listForm = `
                <label>Title</label>
                <input name="title" class="form-control">
                <label>Item ${listCount}</label>
                <input name="item-${listCount}" class="form-control">
                `;

            $('#form-container').html(listForm);
            $('#form-buttons').html('<div class="btn btn-warning container-fluid mt-3" id="add-item">Add</div>');
        } else if ($('#data_style').val() == 'Definition') {
            var dataForm = `
                <label>Title</label>
                <input name="title" class="form-control">
                <label>Definition</label>
                <input name="definition" class="form-control">
                `;

            $('#form-container').html(dataForm);
        } else if ($('#data_style').val() == '3D Print') {
            var dataForm = `
                <label>Title</label>
                <input name="title" class="form-control">
                <label>Description</label>
                <input name="description" class="form-control">
                <label class="d-block">Print</label>
                <input name="image" type="file">
                <div class="row m-0 p-0 mt-2">
                    <div class="col-4 m-0 p-0">
                        <label>Layer Height</label>
                        <input name="layer_height" class="form-control">
                    </div>
                    <div class="col-4 m-0">
                        <label>Density</label>
                        <input name="density"  class="form-control">
                    </div>
                    <div class="col-4 m-0 p-0">
                        <label>Print Length</label>
                        <input name="print_length"  class="form-control">
                    </div>
                </div>
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