<?php

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register the API routes for your application as
| the routes are automatically authenticated using the API guard and
| loaded automatically by this application's RouteServiceProvider.
|
 */

Route::group(['prefix' => 'auth'], function () {
    Route::group(['middleware' => 'auth:api'], function () {
        Route::get('user', 'Auth\AuthController@user');
        Route::get('logout', 'Auth\AuthController@logout');
    });

    Route::post('login', 'Auth\AuthController@login');
    Route::post('register', 'Auth\AuthController@register');
});
