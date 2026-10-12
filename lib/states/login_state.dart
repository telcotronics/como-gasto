import 'package:como_gasto/auth_providers/auth_provider.dart';
import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:shared_preferences/shared_preferences.dart';

class LoginState with ChangeNotifier {
  FirebaseAuth _auth;
  AuthenticationProvider _authenticationProvider;
  AuthenticationProviderFactory _authenticationProviderFactory;

  SharedPreferences _prefs;

  bool _loggedIn = false;
  bool _loading = true;

  FirebaseUser _user;

  // Modificación para publicación en tiendas:
  // Soporte de cuenta demo con credenciales fijas requerida por Google Play Console
  // y Apple App Store para evaluación humana de la app sin depender de servicios externos.
  bool _isDemo = false;
  static const String DEMO_EMAIL = 'demo@comogasto.com';
  static const String DEMO_PIN = '123456';

  bool isDemo() => _isDemo;

  LoginState({
    @required SharedPreferences preferences,
    @required FirebaseAuth firebaseAuth,
    AuthenticationProviderFactory authenticationProviderFactory =
        const AuthenticationProviderFactory(),
  }) {
    _prefs = preferences;
    _auth = firebaseAuth;
    _authenticationProviderFactory = authenticationProviderFactory;
    loginState();
  }

  bool isLoggedIn() => _loggedIn;

  bool isLoading() => _loading;

  FirebaseUser currentUser() => _user;

  // Modificación para publicación en tiendas:
  // Permite iniciar sesión inmediata en modo demo/revisión validando correo y PIN fijos.
  Future<bool> loginDemo({String email = DEMO_EMAIL, String pin = DEMO_PIN}) async {
    if (email.trim().toLowerCase() == DEMO_EMAIL && pin.trim() == DEMO_PIN) {
      _loading = true;
      notifyListeners();

      _isDemo = true;
      _loggedIn = true;
      await _prefs.setBool('isLoggedIn', true);
      await _prefs.setBool('isDemo', true);

      _loading = false;
      notifyListeners();
      return true;
    }
    return false;
  }

  Future<void> login(LoginProvider loginProvider) async {
    _authenticationProvider =
        _authenticationProviderFactory.createAuthProvider(loginProvider);

    _loading = true;
    notifyListeners();

    var authCredentials = await _authenticationProvider.handleSignIn();

    if (authCredentials != null) {
      var authResult = await _auth.signInWithCredential(authCredentials);
      if (authResult != null) {
        _user = authResult.user;
      }
      if (_user != null) {
        print("signed in " + _user.displayName);
      }
    }

    _loading = false;
    _loggedIn = _user != null;
    _prefs.setBool('isLoggedIn', _loggedIn);
    notifyListeners();
  }

  void logout() {
    _prefs.clear();
    if (_authenticationProvider != null) {
      _authenticationProvider.logout();
      _authenticationProvider = null;
    }
    // Modificación para publicación en tiendas:
    // Captura segura de logout en caso de sesión demo sin backend Firebase
    try {
      _auth.signOut();
    } catch (_) {}
    _loggedIn = false;
    _isDemo = false;
    notifyListeners();
  }

  void loginState() async {
    if (_prefs.containsKey('isLoggedIn')) {
      // Modificación para publicación en tiendas:
      // Restauración de sesión demo persistida localmente
      _isDemo = _prefs.getBool('isDemo') ?? false;
      if (_isDemo) {
        _loggedIn = true;
        _loading = false;
        notifyListeners();
        return;
      }
      _user = await _auth.currentUser();
      _loggedIn = _user != null;
      _loading = false;
      notifyListeners();
    } else {
      _loading = false;
      notifyListeners();
    }
  }
}
