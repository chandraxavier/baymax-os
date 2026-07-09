import 'package:web_socket_channel/web_socket_channel.dart';

import '../config/app_config.dart';

class WebSocketClient {
  WebSocketClient({String? url}) : _url = url ?? AppConfig.webSocketUrl;

  final String _url;
  WebSocketChannel? _channel;

  String get url => _url;

  WebSocketChannel? get channel => _channel;
}
