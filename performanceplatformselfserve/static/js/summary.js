$('.js-change').on('click', function () {
    toggleEditMode($(this));
});

$('.js-cancel').on('click', function() {
    toggleEditMode($(this).prev('.js-change'));
});

function toggleEditMode($changeBtn) {
    $changeBtn
        .toggleClass('is-active')
        .html(function (index, oldHtml) {
            return ($.trim(oldHtml) === 'Change' ? 'Save' : 'Change');
        })
        .next('.js-cancel')
        .toggleClass('hidden')
        .closest('.js-edit-group')
        .toggleClass('is-not-editing')
        .find('.form-control, .js-selectable')
        .prop('disabled', function () {
            return !$(this).prop('disabled');
        })
        .first().focus();
}

$('.js-selectable').on('click', function () {
    var isRadio = $(this).attr('type') === 'radio',
        $selectedLabel;
    $selectedLabel = $(this).closest('label');

    $selectedLabel.toggleClass('is-selected');

    if (isRadio) {
        $selectedLabel.siblings('label').removeClass('is-selected');
    }
});

$('textarea').autosize();