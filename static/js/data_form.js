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
        } else if ($('#data_style').val() == 'Image') {
            var dataForm = `
                <label>Title</label>
                <input name="title" class="form-control">
                <label>Description</label>
                <input name="description" class="form-control">
                <label class="d-block">Image</label>
                <input name="image" type="file">
                <div class="btn btn-warning" id="add-attribute">Add Attribute</div>
                <div id="image-attribute-container"></div>
                `;

            $('#form-container').html(dataForm);
        } else if ($('#data_style').val() == 'Code') {
            var dataForm = `
                <label>Title</label>
                <input name="title" class="form-control">
                <label>Code</label>
                <textarea name="code" class="form-control"></textarea>
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

    var attributeCount = 1

    $(document).on('click', '#add-attribute', function() {
        var attriubteInput = `
            <div>
                <label>Title</label>
                <input name="attribute-${attributeCount}" class="form-control">
                <label>Value</label>
                <input name="value-${attributeCount}" class="form-control">
                <hr>
            </div>
        `;

        $('#image-attribute-container').append(attriubteInput);

        attributeCount++
    });

});