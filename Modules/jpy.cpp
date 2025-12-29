#include <windows.h>
struct Ball {
    float x, y;
    float dx, dy;
    float r;
};
Ball ball{50, 50, 3, 3, 20};
LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    switch (msg) {
    case WM_PAINT: {
        PAINTSTRUCT ps;
        HDC hdc = BeginPaint(hwnd, &ps);
        RECT rect;
        GetClientRect(hwnd, &rect);
        int w = rect.right;
        int h = rect.bottom;
        HDC memDC = CreateCompatibleDC(hdc);
        HBITMAP memBM = CreateCompatibleBitmap(hdc, w, h);
        HBITMAP oldBM = (HBITMAP)SelectObject(memDC, memBM);
        HBRUSH bg = CreateSolidBrush(RGB(255,255,255));
        FillRect(memDC, &rect, bg);
        DeleteObject(bg);
        ball.x += ball.dx;
        ball.y += ball.dy;
        if (ball.x - ball.r < 0 || ball.x + ball.r > w)
            ball.dx = -ball.dx;
        if (ball.y - ball.r < 0 || ball.y + ball.r > h)
            ball.dy = -ball.dy;
        HBRUSH red = CreateSolidBrush(RGB(255,0,0));
        HBRUSH old = (HBRUSH)SelectObject(memDC, red);
        Ellipse(memDC,
            (int)(ball.x - ball.r),
            (int)(ball.y - ball.r),
            (int)(ball.x + ball.r),
            (int)(ball.y + ball.r));
        SelectObject(memDC, old);
        DeleteObject(red);
        BitBlt(hdc, 0, 0, w, h, memDC, 0, 0, SRCCOPY);
        SelectObject(memDC, oldBM);
        DeleteObject(memBM);
        DeleteDC(memDC);
        EndPaint(hwnd, &ps);
        return 0;
    }
    case WM_DESTROY:
        PostQuitMessage(0);
        return 0;
    }
    return DefWindowProc(hwnd, msg, wParam, lParam);
}
int WINAPI WinMain(HINSTANCE hInst, HINSTANCE, LPSTR, int nCmdShow) {
    WNDCLASS wc{};
    wc.lpfnWndProc = WndProc;
    wc.hInstance = hInst;
    wc.lpszClassName = "BallWindow";
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW+1);
    RegisterClass(&wc);
    HWND hwnd = CreateWindow(
        "BallWindow", "Bouncing Ball",
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT,
        500, 400,
        nullptr, nullptr, hInst, nullptr
    );
    ShowWindow(hwnd, nCmdShow);
    MSG msg{};
    while (true) {
        while (PeekMessage(&msg, nullptr, 0, 0, PM_REMOVE)) {
            if (msg.message == WM_QUIT)
                return 0;
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
        InvalidateRect(hwnd, nullptr, FALSE);
        Sleep(16);
    }
}
