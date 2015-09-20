QUnit.test( "hello test", function( assert ) {
  assert.ok( 1 == "1", "Passed!" );

});

QUnit.test("smoke test", function( assert ) {
    assert.equal($('.has-error').is(':visible'), true);
    $('.has-error').hide();
    assert.equal($('.has-error').is(':visible'), false);
});

QUnit.test("smoke test2", function( assert ) {
    assert.equal($('.has-error').is(':visible'), true);
    $('.has-error').hide();
    assert.equal($('.has-error').is(':visible'), false);
});

QUnit.test("errors should be hidden on keypress", function( assert ) {
    $('input').trigger('keypress');
    assert.equal($('.has-error').is(':visible'), false);
});

QUnit.test("errors not be hidden unless there is a keypress", function( assert ) {
    assert.equal($('.has-error').is(':visible'), true);
});

