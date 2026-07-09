import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../network/api_client.dart';
import '../network/websocket_client.dart';
import '../router/app_router.dart';
import 'app_logger.dart';

final appLoggerProvider = Provider<AppLogger>((ref) => AppLogger());

final apiClientProvider = Provider<ApiClient>((ref) => ApiClient());

final webSocketClientProvider =
    Provider<WebSocketClient>((ref) => WebSocketClient());

final routerProvider = Provider<GoRouter>((ref) => createAppRouter());
