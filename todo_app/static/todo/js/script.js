$(document).ready(function(){
    if($('#result') != null){
        Read();
    }
    $('#create').on('click', function(){
        $title = $('#title').val();
        $description = $('#description').val();
        $status = $('#status').val();
        $task_date = $('#task_date').val();

        if($title == "" || $description == "" || $status == "" || $task_date == ""){
            alert("Please complete the required field");
        }else{
            $.ajax({
                url: 'create',
                type: 'POST',
                data: {
                    title: $title,
                    description: $description,
                    status: $status,
                    task_date: $task_date,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
                    Read();
                    $('#title').val('');
                    $('#description').val('');
                    $('#status').val('');
                    $('#task_date').val('');
                }
            });
        }
    });

    $(document).on('click', '.edit', function(){
        $id = $(this).attr('name');
        window.location = "edit/" + $id;
    });

    $('#update').on('click', function(){
        $title = $('#title').val();
        $description = $('#description').val();
        $status = $('#status').val();
        $task_date = $('#task_date').val();

        if($title == "" || $description == "" || $status == "" || $task_date == ""){
            alert("Please complete the required field");
        }else{
            $id = $('#todo_id').val();
            $.ajax({
                url: 'update/' + $id,
                type: 'POST',
                data: {
                    title: $title,
                    description: $description,
                    status: $status,
                    task_date: $task_date,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
                    window.location.href = "/";
                    alert('Updated!');
                }
            });
        }

    });

    $(document).on('click', '.delete', function(){
        $id = $(this).attr('name');
        $.ajax({
            url: 'delete/' + $id,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(){
                Read();
                alert("Deleted!");
            }
        });
    });

});

function Read(){
    $.ajax({
		url: 'read',
		type: 'GET',
		async: false,
		success: function(response){
			$('#result').html(response);
		}
    });
}