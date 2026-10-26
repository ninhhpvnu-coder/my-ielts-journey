/**
 * IELTS Journey with Ms Ninh — Professional Security Gateway & Member Portal
 * (C) 2026 - 2028 IELTS Journey with Ms Ninh. All rights reserved.
 * 
 * Features:
 * - Device Fingerprinting & Single-Device Session Lock
 * - Cryptographic Key Verification (HMAC-FNV1a Checksum)
 * - 4 Roadmap Tiers Access Control (Units 1-2 Free Trial, Units 3-30 Paywall)
 * - Anti-Theft Shield (Anti-RightClick, Anti-F12, Anti-Ctrl+U, Anti-Inspect)
 * - Dynamic Anti-Recording Watermark Injection
 * - Paywall & Student Activation Modal
 */

(function (window) {
    'use strict';

    const IELTS_SALT = "NINH_2026_IELTS_SALT";
    const STORAGE_KEY_STUDENT = "ielts_student_profile";
    const STORAGE_KEY_DEVICE = "ielts_device_fingerprint";
    const STORAGE_KEY_KEYS_VAULT = "ielts_admin_issued_keys";
    const STORAGE_KEY_ADMIN = "ielts_admin_authenticated";
    const STORAGE_KEY_PAYMENT = "ielts_payment_config";
    const STORAGE_KEY_TARGET = "ielts_student_target";
    const STORAGE_KEY_STREAK = "ielts_streak_data";
    const STORAGE_KEY_MISTAKES = "ielts_mistakes_notebook";
    const STORAGE_KEY_MASTER_PROGRESS = "ielts_master_progress_v1";

    const DEFAULT_PAYMENT_CONFIG = {
        bankId: "TCB",
        bankName: "Techcombank",
        accountNumber: "366566999999",
        accountName: "NGO THI NINH",
        amount: 150000,
        amountFormatted: "150.000 VNĐ",
        hotlineZalo: "0869669659",
        zaloLink: "https://zalo.me/0869669659"
    };

    const TIERS_META = {
        'FD': { name: 'Giáo Trình Foundation (30 Units)', color: '#38bdf8', icon: '📚' },
        'B5': { name: 'Giáo Trình Band 5.0 — 6.0', color: '#10b981', icon: '🌱' },
        'B6': { name: 'Giáo Trình Band 6.0 — 7.5', color: '#f59e0b', icon: '⚡' },
        'CAM': { name: 'Luyện Đề Cambridge 8.0+', color: '#a855f7', icon: '🏆' },
        'VIP': { name: 'VIP Toàn Diện (Tất Cả 4 Khóa Học)', color: '#f43f5e', icon: '👑' }
    };

    const IELTSAuth = {
        // --- 000. ACADEMIC PAPER & MIDNIGHT THEME ENGINE ---
        getTheme: function () {
            return localStorage.getItem('ielts_theme') || 'paper';
        },

        initTheme: function () {
            const theme = this.getTheme();
            document.documentElement.setAttribute('data-theme', theme);
            this.updateThemePillUI(theme);
        },

        toggleTheme: function () {
            const current = this.getTheme();
            const next = (current === 'paper') ? 'dark' : 'paper';
            localStorage.setItem('ielts_theme', next);
            document.documentElement.setAttribute('data-theme', next);
            this.updateThemePillUI(next);
            this.showSecurityToast(next === 'paper' ? '☀️ Đã bật Chế độ Giấy Ngà Học Thuật (Chống mỏi mắt)' : '🌙 Đã bật Chế độ Ban Đêm (Midnight Navy)');
            // Update passport modal if open
            const passportModal = document.getElementById('ielts_passport_modal');
            if (passportModal && passportModal.style.display === 'flex') {
                this.refreshPassportUI();
            }
        },

        updateThemePillUI: function (theme) {
            document.querySelectorAll('.theme-switch-pill, .theme-toggle-btn').forEach(btn => {
                if (theme === 'paper') {
                    btn.innerHTML = `☀️ <span class="theme-text">Giấy Ngà Học Thuật</span>`;
                    btn.title = "Đang ở Chế độ Giấy Ngà. Bấm để chuyển sang Chế độ Ban Đêm";
                } else {
                    btn.innerHTML = `🌙 <span class="theme-text">Ban Đêm (Midnight)</span>`;
                    btn.title = "Đang ở Chế độ Ban Đêm. Bấm để chuyển sang Chế độ Giấy Ngà Học Thuật";
                }
            });
        },

        // --- 00. MASTER ADMIN & OWNER DETECTION ---
        isAdminOwner: function () {
            return (sessionStorage.getItem(STORAGE_KEY_ADMIN) === 'true' || localStorage.getItem(STORAGE_KEY_ADMIN) === 'true');
        },

        setAdminOwner: function (enabled) {
            if (enabled) {
                sessionStorage.setItem(STORAGE_KEY_ADMIN, 'true');
                localStorage.setItem(STORAGE_KEY_ADMIN, 'true');
            } else {
                sessionStorage.removeItem(STORAGE_KEY_ADMIN);
                localStorage.removeItem(STORAGE_KEY_ADMIN);
            }
        },
        // --- 0. PAYMENT CONFIG & VIETQR ENGINE ---
        getPaymentConfig: function () {
            try {
                const stored = localStorage.getItem(STORAGE_KEY_PAYMENT);
                if (stored) {
                    return { ...DEFAULT_PAYMENT_CONFIG, ...JSON.parse(stored) };
                }
            } catch (e) {}
            return { ...DEFAULT_PAYMENT_CONFIG };
        },

        savePaymentConfig: function (cfg) {
            localStorage.setItem(STORAGE_KEY_PAYMENT, JSON.stringify(cfg));
        },

        buildVietQRUrl: function (phone, amount) {
            const cfg = this.getPaymentConfig();
            const finalAmt = amount || cfg.amount || 150000;
            const cleanPhone = (phone || '').replace(/[^0-9]/g, '');
            const memo = cleanPhone.length >= 6 ? `IELTS FD ${cleanPhone}` : 'IELTS FD 30 UNITS';
            const encodedMemo = encodeURIComponent(memo);
            const encodedName = encodeURIComponent(cfg.accountName);
            return `https://img.vietqr.io/image/${cfg.bankId}-${cfg.accountNumber}-compact2.png?amount=${finalAmt}&addInfo=${encodedMemo}&accountName=${encodedName}`;
        },

        updateRegisterVietQR: function () {
            const phone = (document.getElementById('reg_student_phone')?.value || '').trim();
            const qrImg = document.getElementById('reg_vietqr_img');
            const memoEl = document.getElementById('reg_transfer_memo');
            const zaloBtn = document.getElementById('reg_zalo_btn');
            const cfg = this.getPaymentConfig();

            const cleanPhone = phone.replace(/[^0-9]/g, '');
            const memo = cleanPhone.length >= 6 ? `IELTS FD ${cleanPhone}` : 'IELTS FD [SĐT_CỦA_BẠN]';
            if (memoEl) memoEl.textContent = memo;

            if (qrImg) {
                qrImg.src = this.buildVietQRUrl(cleanPhone);
            }

            if (zaloBtn) {
                const name = (document.getElementById('reg_student_name')?.value || '').trim();
                const studentInfo = name ? `em là ${name} (SĐT: ${cleanPhone || '...'}), ` : '';
                const msg = encodeURIComponent(`Chào Cô Ninh, ${studentInfo}em vừa chuyển khoản 150.000đ đăng ký khóa học IELTS Foundation 30 Units (Cú pháp CK: ${memo}). Nhờ cô kiểm tra và gửi mã kích hoạt giúp em với ạ!`);
                zaloBtn.href = `https://zalo.me/${cfg.hotlineZalo}?text=${msg}`;
            }
        },

        switchToActivateWithPrefill: function () {
            const name = (document.getElementById('reg_student_name')?.value || '').trim();
            const phone = (document.getElementById('reg_student_phone')?.value || '').trim();
            this.switchModalTab('activate');
            if (name) {
                const nInput = document.getElementById('auth_student_name');
                if (nInput) nInput.value = name;
            }
            if (phone) {
                const cInput = document.getElementById('auth_student_contact');
                if (cInput) cInput.value = phone;
            }
            const kInput = document.getElementById('auth_student_key');
            if (kInput) kInput.focus();
        },

        // --- 1. DEVICE FINGERPRINTING ---
        getDeviceId: function () {
            let devId = localStorage.getItem(STORAGE_KEY_DEVICE);
            if (!devId) {
                const screenProps = `${window.screen.width}x${window.screen.height}x${window.screen.colorDepth}`;
                const navProps = `${navigator.userAgent}-${navigator.language}-${navigator.hardwareConcurrency || 4}`;
                const tz = (Intl && Intl.DateTimeFormat) ? Intl.DateTimeFormat().resolvedOptions().timeZone : 'UTC';
                const raw = `${screenProps}-${navProps}-${tz}-${Date.now()}-${Math.random()}`;
                
                let h = 0x811c9dc5;
                for (let i = 0; i < raw.length; i++) {
                    h = Math.imul(h ^ raw.charCodeAt(i), 0x01000193) >>> 0;
                }
                devId = 'DEV-' + ('00000000' + h.toString(16).toUpperCase()).slice(-8);
                localStorage.setItem(STORAGE_KEY_DEVICE, devId);
            }
            return devId;
        },

        // --- 2. CRYPTOGRAPHIC CHECKSUM & KEY GENERATOR ---
        calcSignature: function (tier, code) {
            const raw = `${IELTS_SALT}_${tier.toUpperCase()}_${code.toUpperCase()}`;
            let h = 0x811c9dc5;
            for (let i = 0; i < raw.length; i++) {
                h = Math.imul(h ^ raw.charCodeAt(i), 0x01000193) >>> 0;
            }
            return ('00000000' + h.toString(16).toUpperCase()).slice(-8).substring(0, 4);
        },

        generateKey: function (tier, customCode) {
            tier = (tier || 'FD').toUpperCase();
            const code = customCode ? customCode.toUpperCase() : Math.floor(1000 + Math.random() * 9000).toString();
            const sig = this.calcSignature(tier, code);
            return `NINH-${tier}-${code}-${sig}`;
        },

        verifyKey: function (keyStr) {
            if (!keyStr || typeof keyStr !== 'string') return { valid: false, error: 'Mã không hợp lệ' };
            const clean = keyStr.trim().toUpperCase();
            const parts = clean.split('-');
            if (parts.length !== 4 || parts[0] !== 'NINH') {
                return { valid: false, error: 'Định dạng mã không đúng (Cần có dạng NINH-XX-XXXX-XXXX)' };
            }
            const tier = parts[1];
            const code = parts[2];
            const sig = parts[3];

            if (!TIERS_META[tier]) {
                return { valid: false, error: 'Mã gói học không tồn tại trong hệ thống' };
            }

            const expectedSig = this.calcSignature(tier, code);
            if (sig !== expectedSig) {
                return { valid: false, error: 'Mã kích hoạt không hợp lệ hoặc đã bị thay đổi' };
            }

            return { valid: true, tier: tier, tierName: TIERS_META[tier].name, key: clean };
        },

        // --- 3. STUDENT PROFILE & SINGLE-DEVICE SESSION ---
        getStudent: function () {
            try {
                const data = localStorage.getItem(STORAGE_KEY_STUDENT);
                if (!data) return null;
                const profile = JSON.parse(data);
                // Check single device lock
                const currentDev = this.getDeviceId();
                if (profile.deviceId && profile.deviceId !== currentDev) {
                    profile.isDeviceMismatch = true;
                }
                return profile;
            } catch (e) {
                return null;
            }
        },

        activateStudent: function (name, contact, keyStr) {
            const verification = this.verifyKey(keyStr);
            if (!verification.valid) {
                return { success: false, error: verification.error };
            }

            if (!name || name.trim().length < 2) {
                return { success: false, error: 'Vui lòng nhập họ và tên của học viên' };
            }

            if (!contact || contact.trim().length < 6) {
                return { success: false, error: 'Vui lòng nhập số điện thoại hoặc email liên hệ' };
            }

            const currentDev = this.getDeviceId();
            const profile = {
                name: name.trim(),
                contact: contact.trim(),
                key: verification.key,
                tier: verification.tier,
                tierName: verification.tierName,
                deviceId: currentDev,
                activatedAt: new Date().toISOString()
            };

            localStorage.setItem(STORAGE_KEY_STUDENT, JSON.stringify(profile));

            // Record into local vault for admin audit
            this.recordKeyUsage(profile);

            return { success: true, profile: profile };
        },

        recordKeyUsage: function (profile) {
            try {
                let vault = JSON.parse(localStorage.getItem(STORAGE_KEY_KEYS_VAULT) || '[]');
                const idx = vault.findIndex(item => item.key === profile.key);
                if (idx >= 0) {
                    vault[idx] = { ...vault[idx], ...profile, lastUsed: new Date().toISOString() };
                } else {
                    vault.push({ ...profile, registeredAt: new Date().toISOString() });
                }
                localStorage.setItem(STORAGE_KEY_KEYS_VAULT, JSON.stringify(vault));
            } catch (e) {}
        },

        logout: function () {
            localStorage.removeItem(STORAGE_KEY_STUDENT);
            window.location.reload();
        },

        // --- 4. ACCESS GUARD FOR UNITS ---
        hasAccessToUnit: function (unitNum) {
            // Master Admin Owner (Ms Ninh) has 100% UNRESTRICTED FULL ACCESS!
            if (this.isAdminOwner()) {
                return {
                    allowed: true,
                    isFreeTrial: false,
                    isMasterAdmin: true,
                    student: { name: 'Cô Ninh (Chủ Sở Hữu)', tier: 'VIP', tierName: 'Chủ Sở Hữu Hệ Thống' }
                };
            }

            const num = parseInt(unitNum, 10);
            // Units 1 and 2 are 100% FREE TRIAL for all visitors!
            if (num === 1 || num === 2) {
                return { allowed: true, isFreeTrial: true };
            }

            const student = this.getStudent();
            if (!student) {
                return { allowed: false, reason: 'NOT_LOGGED_IN' };
            }

            if (student.isDeviceMismatch) {
                return { allowed: false, reason: 'DEVICE_MISMATCH', student: student };
            }

            // Foundation covers Units 1-30. VIP covers everything.
            if (student.tier === 'FD' || student.tier === 'VIP') {
                return { allowed: true, isFreeTrial: false, student: student };
            }

            return { allowed: false, reason: 'WRONG_TIER', student: student };
        },

        guardUnitPage: function (unitNum) {
            const access = this.hasAccessToUnit(unitNum);
            if (access.allowed) {
                // If allowed, inject security watermarks & features
                this.initAntiTheft();
                this.injectWatermark(access.student, access.isFreeTrial);
                this.injectUnitTopAuthBadge(access);
                return;
            }

            // If not allowed, lock screen immediately with luxury paywall blocker
            this.initAntiTheft();
            this.renderPageBlocker(unitNum, access.reason);
        },

        // --- 5. ANTI-THEFT & ANTI-PIRACY SHIELD ---
        initAntiTheft: function () {
            // Disable right click context menu
            document.addEventListener('contextmenu', function (e) {
                e.preventDefault();
                IELTSAuth.showSecurityToast('🔒 Bản quyền độc quyền thuộc "IELTS Journey with Ms Ninh". Tính năng sao chép bị vô hiệu hóa.');
                return false;
            });

            // Block inspection keyboard shortcuts
            document.addEventListener('keydown', function (e) {
                // F12
                if (e.key === 'F12' || e.keyCode === 123) {
                    e.preventDefault();
                    IELTSAuth.showSecurityToast('🔒 Phím chức năng quản trị bị vô hiệu hóa.');
                    return false;
                }
                // Ctrl+Shift+I / Ctrl+Shift+J / Ctrl+Shift+C / Ctrl+U / Ctrl+S / Ctrl+P
                if (e.ctrlKey || e.metaKey) {
                    const k = (e.key || '').toLowerCase();
                    if (k === 'u' || k === 's' || k === 'p' || (e.shiftKey && (k === 'i' || k === 'j' || k === 'c'))) {
                        e.preventDefault();
                        IELTSAuth.showSecurityToast('🔒 Thao tác trích xuất mã nguồn bị vô hiệu hóa để bảo vệ bản quyền.');
                        return false;
                    }
                }
            });

            // Console security warning
            try {
                setTimeout(function () {
                    console.clear();
                    console.log("%c🪷 IELTS Journey with Ms Ninh — Bản Quyền Sở Hữu Trí Tuệ", "color: #c58b62; font-size: 18px; font-weight: bold;");
                    console.log("%cHệ thống giáo trình & dữ liệu bài tập chuẩn Cambridge (2026 - 2028) được bảo hộ pháp lý.\nMọi hành vi sao chép, trích xuất mã nguồn hoặc chia sẻ tài khoản trái phép đều bị nghiêm cấm.", "color: #94a3b8; font-size: 13px;");
                }, 500);
            } catch (e) {}
        },

        showSecurityToast: function (msg) {
            let toast = document.getElementById('ielts_security_toast');
            if (!toast) {
                toast = document.createElement('div');
                toast.id = 'ielts_security_toast';
                toast.style.cssText = `
                    position: fixed;
                    bottom: 24px;
                    left: 50%;
                    transform: translateX(-50%) translateY(100px);
                    background: rgba(15, 23, 42, 0.95);
                    border: 1.5px solid rgba(197, 139, 98, 0.6);
                    color: #f8fafc;
                    padding: 12px 24px;
                    border-radius: 999px;
                    font-size: 0.88rem;
                    font-weight: 600;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.7), 0 0 20px rgba(197, 139, 98, 0.3);
                    z-index: 999999;
                    pointer-events: none;
                    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
                    opacity: 0;
                    text-align: center;
                    max-width: 90vw;
                `;
                document.body.appendChild(toast);
            }
            toast.textContent = msg;
            toast.style.opacity = '1';
            toast.style.transform = 'translateX(-50%) translateY(0)';
            clearTimeout(this._toastTimer);
            this._toastTimer = setTimeout(() => {
                toast.style.opacity = '0';
                toast.style.transform = 'translateX(-50%) translateY(100px)';
            }, 3200);
        },

        // --- 6. DYNAMIC ANTI-RECORDING WATERMARK ---
        injectWatermark: function (student, isFreeTrial) {
            if (document.getElementById('ielts_watermark_layer')) return;
            const container = document.createElement('div');
            container.id = 'ielts_watermark_layer';
            container.style.cssText = `
                position: fixed;
                inset: 0;
                pointer-events: none;
                z-index: 9999;
                overflow: hidden;
                opacity: 0.07;
                display: flex;
                flex-wrap: wrap;
                align-content: space-around;
                justify-content: space-around;
                user-select: none;
            `;

            let watermarkText = "🪷 IELTS Journey with Ms Ninh • Bản Học Thử (Free Trial)";
            if (student) {
                watermarkText = `🪷 IELTS Journey with Ms Ninh • Học viên: ${student.name} • ${student.contact} • [${student.deviceId || 'DEV'}]`;
            }

            for (let i = 0; i < 18; i++) {
                const mark = document.createElement('div');
                mark.textContent = watermarkText;
                mark.style.cssText = `
                    transform: rotate(-22deg);
                    font-size: 13px;
                    font-weight: 700;
                    color: #fff;
                    white-space: nowrap;
                    padding: 30px 40px;
                    letter-spacing: 1px;
                    text-shadow: 0 1px 2px rgba(0,0,0,0.8);
                `;
                container.appendChild(mark);
            }
            document.body.appendChild(container);
        },

        injectUnitTopAuthBadge: function (access) {
            // Find navbar or container to put student indicator
            const bar = document.querySelector('.unit-nav-bar') || document.querySelector('.header') || document.querySelector('header');
            if (!bar) return;

            const badge = document.createElement('div');
            badge.style.cssText = `
                display: inline-flex;
                align-items: center;
                gap: 8px;
                background: rgba(15, 23, 42, 0.75);
                border: 1px solid rgba(197, 139, 98, 0.35);
                padding: 4px 12px;
                border-radius: 999px;
                font-size: 0.75rem;
                color: #e2e8f0;
                margin-left: auto;
            `;

            if (access.isMasterAdmin) {
                badge.style.borderColor = 'rgba(197, 139, 98, 0.7)';
                badge.style.background = 'radial-gradient(circle at 10% 10%, rgba(197, 139, 98, 0.25) 0%, rgba(15, 23, 42, 0.9) 70%)';
                badge.innerHTML = `<span>👑 <b>Cô Ninh (Chủ Sở Hữu)</b></span> <span style="color: #34d399;">• Toàn Quyền Quản Trị</span> <a href="admin.html" style="color: #38bdf8; text-decoration: underline; margin-left: 6px;">Quản Trị ⚙️</a>`;
            } else if (access.isFreeTrial) {
                badge.innerHTML = `<span>✨ <b>Học Thử Miễn Phí (Unit 01-02)</b></span> <a href="index.html#activate" style="color: #38bdf8; text-decoration: underline; margin-left: 6px;">Kích hoạt trọn bộ 30 Unit</a>`;
            } else if (access.student) {
                badge.innerHTML = `<span>🎓 Học viên: <b style="color: #38bdf8;">${access.student.name}</b></span> <button onclick="IELTSAuth.toggleTheme()" class="theme-switch-pill" style="display: inline-flex; align-items: center; gap: 5px; background: rgba(197, 133, 93, 0.15); border: 1.5px solid rgba(197, 133, 93, 0.45); color: var(--accent, #c5855d); padding: 6px 12px; border-radius: 999px; font-size: 0.78rem; font-weight: 700; cursor: pointer;">☀️ <span class="theme-text">Giấy Ngà</span></button>
                            <button onclick="IELTSAuth.openPassportModal()" style="background: linear-gradient(135deg, #14324d, #1d4367); color: #fff; border: none; color: #0b1120; border-radius: 6px; padding: 2px 8px; font-size: 0.7rem; font-weight: 800; cursor: pointer; margin-left: 4px;">🎓 Hồ Sơ & Sổ Tay</button>`;
            }
            bar.appendChild(badge);
        },

        // --- 7. LUXURY PAYWALL BLOCKER FOR LOCKED UNITS ---
        renderPageBlocker: function (unitNum, reason) {
            // Hide main content
            const allBodyChildren = Array.from(document.body.children);
            allBodyChildren.forEach(el => {
                if (el.tagName !== 'SCRIPT' && el.tagName !== 'STYLE') {
                    el.style.filter = 'blur(16px)';
                    el.style.pointerEvents = 'none';
                    el.style.userSelect = 'none';
                }
            });

            const blocker = document.createElement('div');
            blocker.id = 'ielts_fullscreen_blocker';
            blocker.style.cssText = `
                position: fixed;
                inset: 0;
                background: rgba(11, 17, 32, 0.94);
                backdrop-filter: blur(20px);
                z-index: 9999999;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            `;

            let reasonTitle = "🔒 BÀI HỌC THUỘC GIÁO TRÌNH BẢN QUYỀN";
            let reasonDesc = `Bài học <b>Unit ${unitNum}</b> nằm trong hệ thống giáo trình độc quyền 30 Units của <b>IELTS Journey with Ms Ninh</b>.`;

            if (reason === 'DEVICE_MISMATCH') {
                reasonTitle = "⚠️ PHÁT HIỆN THAY ĐỔI THIẾT BỊ HỌC TẬP";
                reasonDesc = `Tài khoản của bạn đã được liên kết với một thiết bị khác (Single-Device Lock). Để bảo mật, mỗi mã kích hoạt chỉ sử dụng trên 1 thiết bị chính thức. Vui lòng liên hệ Cô Ninh nếu bạn vừa đổi máy tính/điện thoại mới.`;
            } else if (reason === 'WRONG_TIER') {
                reasonTitle = "🔒 CẦN NÂNG CẤP GÓI HỌC FOUNDATION";
                reasonDesc = `Mã kích hoạt hiện tại của bạn không bao gồm quyền truy cập lộ trình Foundation 30 Units. Vui lòng nâng cấp gói học để mở khóa toàn bộ bài giảng.`;
            }

            blocker.innerHTML = `
                <div style="background: linear-gradient(135deg, rgba(30, 41, 59, 0.98), rgba(15, 23, 42, 0.98)); border: 1.5px solid rgba(197, 139, 98, 0.45); border-radius: 24px; padding: 36px 30px; max-width: 520px; width: 100%; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8), 0 0 35px rgba(197, 139, 98, 0.25); text-align: center; color: #f8fafc; font-family: 'Plus Jakarta Sans', sans-serif;">
                    <div style="width: 80px; height: 80px; margin: 0 auto 18px; border-radius: 20px; background: rgba(197, 139, 98, 0.12); border: 1.5px solid rgba(197, 139, 98, 0.4); display: flex; align-items: center; justify-content: center; font-size: 36px; box-shadow: 0 0 20px rgba(197, 139, 98, 0.2);">
                        🔒
                    </div>
                    <div style="font-size: 0.8rem; font-weight: 800; color: #c58b62; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 6px;">IELTS Journey with Ms Ninh</div>
                    <h2 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.35rem; color: #fff; margin-bottom: 12px; line-height: 1.3;">${reasonTitle}</h2>
                    <p style="font-size: 0.9rem; color: #94a3b8; line-height: 1.6; margin-bottom: 24px;">${reasonDesc}</p>
                    
                    <div style="display: flex; flex-direction: column; gap: 12px;">
                        <button onclick="IELTSAuth.openPaywallModal()" style="background: linear-gradient(135deg, #38bdf8, #0284c7); color: #0b1120; border: none; font-weight: 800; font-size: 0.95rem; padding: 14px 20px; border-radius: 12px; cursor: pointer; box-shadow: 0 0 20px rgba(56, 189, 248, 0.35); transition: transform 0.2s;">
                            🔑 Nhập Mã Kích Hoạt Khóa Học
                        </button>
                        <a href="index.html" style="background: rgba(51, 65, 85, 0.6); color: #e2e8f0; border: 1px solid #475569; font-weight: 700; font-size: 0.9rem; padding: 12px 20px; border-radius: 12px; text-decoration: none; transition: background 0.2s;">
                            ← Quay lại Trang Chủ (Học thử Unit 1 & 2 miễn phí)
                        </a>
                    </div>

                    <div style="margin-top: 24px; padding-top: 18px; border-top: 1px solid rgba(148, 163, 184, 0.15); font-size: 0.8rem; color: #64748b;">
                        Đăng ký nhận mã bản quyền: Hotline / Zalo Cô Ninh • Hỗ trợ bảo vệ tác quyền 24/7
                    </div>
                </div>
            `;
            document.body.appendChild(blocker);
        },

        // --- 8. PAYWALL & ACTIVATION MODAL (IN INDEX & ANYWHERE) ---
        openPaywallModal: function () {
            let modal = document.getElementById('ielts_paywall_modal');
            if (!modal) {
                modal = document.createElement('div');
                modal.id = 'ielts_paywall_modal';
                modal.style.cssText = `
                    position: fixed;
                    inset: 0;
                    background: rgba(11, 17, 32, 0.85);
                    backdrop-filter: blur(12px);
                    z-index: 10000000;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 16px;
                `;

                modal.innerHTML = `
                    <div style="background: #1e293b; border: 1.5px solid rgba(197, 139, 98, 0.45); border-radius: 24px; max-width: 540px; width: 100%; box-shadow: 0 25px 60px rgba(0,0,0,0.85), 0 0 30px rgba(197, 139, 98, 0.2); overflow: hidden; animation: popIn 0.25s ease-out; font-family: 'Plus Jakarta Sans', sans-serif;">
                        <!-- Modal Header -->
                        <div style="padding: 20px 24px; background: linear-gradient(135deg, rgba(30, 41, 59, 1), rgba(15, 23, 42, 1)); border-bottom: 1px solid rgba(197, 139, 98, 0.3); display: flex; justify-content: space-between; align-items: center;">
                            <div style="display: flex; align-items: center; gap: 12px;">
                                <div style="font-size: 24px;">🪷</div>
                                <div>
                                    <div style="font-size: 0.75rem; color: #c58b62; font-weight: 800; letter-spacing: 1px; text-transform: uppercase;">IELTS Journey with Ms Ninh</div>
                                    <div style="font-size: 1.1rem; color: #fff; font-weight: 700;">Cổng Kích Hoạt & Bản Quyền Học Viên</div>
                                </div>
                            </div>
                            <button onclick="IELTSAuth.closePaywallModal()" style="background: none; border: none; color: #94a3b8; font-size: 24px; cursor: pointer; padding: 4px 8px; line-height: 1;">&times;</button>
                        </div>

                        <!-- Modal Tabs -->
                        <div style="display: flex; border-bottom: 1px solid #334155; background: #0f172a;">
                            <button id="tab_btn_activate" onclick="IELTSAuth.switchModalTab('activate')" style="flex: 1; padding: 14px; background: none; border: none; border-bottom: 2px solid #38bdf8; color: #38bdf8; font-weight: 700; font-size: 0.88rem; cursor: pointer;">
                                🔑 Nhập Mã Kích Hoạt
                            </button>
                            <button id="tab_btn_register" onclick="IELTSAuth.switchModalTab('register')" style="flex: 1; padding: 14px; background: none; border: none; border-bottom: 2px solid transparent; color: #94a3b8; font-weight: 700; font-size: 0.88rem; cursor: pointer;">
                                💳 Đăng Ký Khóa Học
                            </button>
                        </div>

                        <!-- Tab 1: Kích Hoạt -->
                        <div id="modal_tab_activate" style="padding: 24px;">
                            <div style="margin-bottom: 14px;">
                                <label style="display: block; font-size: 0.82rem; font-weight: 700; color: #cbd5e1; margin-bottom: 6px;">Họ và Tên Học Viên *</label>
                                <input type="text" id="auth_student_name" placeholder="Ví dụ: Nguyễn Văn An" style="width: 100%; box-sizing: border-box; background: #0b1120; border: 1px solid #334155; border-radius: 10px; padding: 11px 14px; color: #fff; font-size: 0.9rem;">
                            </div>
                            <div style="margin-bottom: 14px;">
                                <label style="display: block; font-size: 0.82rem; font-weight: 700; color: #cbd5e1; margin-bottom: 6px;">Số Điện Thoại / Email nhận khóa học *</label>
                                <input type="text" id="auth_student_contact" placeholder="Số điện thoại hoặc Email của bạn" style="width: 100%; box-sizing: border-box; background: #0b1120; border: 1px solid #334155; border-radius: 10px; padding: 11px 14px; color: #fff; font-size: 0.9rem;">
                            </div>
                            <div style="margin-bottom: 18px;">
                                <label style="display: block; font-size: 0.82rem; font-weight: 700; color: #cbd5e1; margin-bottom: 6px;">Mã Kích Hoạt Bản Quyền (Activation Key) *</label>
                                <input type="text" id="auth_student_key" placeholder="NINH-FD-XXXX-YYYY" style="width: 100%; box-sizing: border-box; background: #0b1120; border: 1.5px solid rgba(197, 139, 98, 0.6); border-radius: 10px; padding: 11px 14px; color: #38bdf8; font-size: 1.05rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase;">
                                <div style="font-size: 0.74rem; color: #94a3b8; margin-top: 5px;">Mã do Cô Ninh cấp sau khi hoàn tất đăng ký khóa học.</div>
                            </div>
                            <div id="auth_msg_box" style="display: none; padding: 10px 14px; border-radius: 10px; font-size: 0.85rem; margin-bottom: 16px;"></div>

                            <button onclick="IELTSAuth.submitActivation()" style="width: 100%; background: linear-gradient(135deg, #38bdf8, #0284c7); color: #0b1120; border: none; font-weight: 800; font-size: 1rem; padding: 13px; border-radius: 12px; cursor: pointer; box-shadow: 0 0 20px rgba(56, 189, 248, 0.4);">
                                🔓 Xác Nhận Kích Hoạt Bản Quyền
                            </button>
                        </div>

                        <!-- Tab 2: Đăng Ký Mới & Thanh Toán VietQR -->
                        <div id="modal_tab_register" style="padding: 22px 24px; max-height: 80vh; overflow-y: auto; display: none;">
                            <!-- Course & Tuition Fee -->
                            <div style="background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.9)); border: 1px solid rgba(197, 139, 98, 0.4); border-radius: 16px; padding: 16px; margin-bottom: 18px;">
                                <div style="display: flex; justify-content: space-between; align-items: center; gap: 10px;">
                                    <div>
                                        <div style="font-size: 0.75rem; font-weight: 800; color: #c58b62; text-transform: uppercase; letter-spacing: 1px;">Khóa Học Trực Tuyến 24/7</div>
                                        <div style="font-size: 1rem; font-weight: 800; color: #fff; margin-top: 2px;">📚 IELTS Foundation (30 Units)</div>
                                    </div>
                                    <div style="text-align: right; flex-shrink: 0;">
                                        <div style="font-size: 0.75rem; color: #94a3b8;">Học phí:</div>
                                        <div style="font-size: 1.35rem; font-weight: 800; color: #34d399;">150.000 VNĐ</div>
                                    </div>
                                </div>
                            </div>

                            <!-- Step 1: Student Contact -->
                            <div style="margin-bottom: 16px;">
                                <div style="font-size: 0.82rem; font-weight: 700; color: #38bdf8; margin-bottom: 8px;">
                                    BƯỚC 1: Nhập thông tin để tự động tạo mã VietQR
                                </div>
                                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 10px;">
                                    <div>
                                        <label style="display: block; font-size: 0.78rem; font-weight: 700; color: #cbd5e1; margin-bottom: 4px;">Họ và Tên *</label>
                                        <input type="text" id="reg_student_name" placeholder="Nguyễn Văn An" oninput="IELTSAuth.updateRegisterVietQR()" style="width: 100%; box-sizing: border-box; background: #0b1120; border: 1px solid #334155; border-radius: 8px; padding: 9px 12px; color: #fff; font-size: 0.88rem;">
                                    </div>
                                    <div>
                                        <label style="display: block; font-size: 0.78rem; font-weight: 700; color: #cbd5e1; margin-bottom: 4px;">Số Điện Thoại / Zalo *</label>
                                        <input type="tel" id="reg_student_phone" placeholder="0988xxxxxx" oninput="IELTSAuth.updateRegisterVietQR()" style="width: 100%; box-sizing: border-box; background: #0b1120; border: 1.5px solid rgba(56, 189, 248, 0.5); border-radius: 8px; padding: 9px 12px; color: #38bdf8; font-size: 0.88rem; font-weight: 700;">
                                    </div>
                                </div>
                            </div>

                            <!-- Step 2: VietQR Box -->
                            <div style="background: #0f172a; border: 1.5px solid rgba(197, 139, 98, 0.4); border-radius: 16px; padding: 18px; margin-bottom: 16px; text-align: center;">
                                <div style="font-size: 0.78rem; font-weight: 800; color: #c58b62; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px;">
                                    BƯỚC 2: Quét Mã VietQR Bằng Ứng Dụng Ngân Hàng
                                </div>
                                
                                <div style="display: flex; justify-content: center; margin-bottom: 14px;">
                                    <img id="reg_vietqr_img" src="https://img.vietqr.io/image/TCB-366566999999-compact2.png?amount=150000&addInfo=IELTS%20FD&accountName=NGO%20THI%20NINH" alt="Techcombank VietQR" style="width: 210px; height: auto; border-radius: 14px; background: #fff; padding: 6px; box-shadow: 0 10px 25px rgba(0,0,0,0.6);">
                                </div>

                                <!-- Bank Text Info with 1-Click Copy -->
                                <div style="text-align: left; background: #0b1120; border: 1px solid #334155; border-radius: 12px; padding: 12px; font-size: 0.82rem; line-height: 1.8;">
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #94a3b8;">Ngân hàng:</span>
                                        <span style="font-weight: 800; color: #fff;">Techcombank (TCB)</span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #94a3b8;">Số tài khoản:</span>
                                        <span style="display: flex; align-items: center; gap: 6px;">
                                            <b style="color: #38bdf8; font-family: monospace; font-size: 0.95rem;">366566999999</b>
                                            <button onclick="navigator.clipboard.writeText('366566999999'); IELTSAuth.showSecurityToast('✓ Đã sao chép Số tài khoản Techcombank!');" style="background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8; border-radius: 4px; padding: 2px 6px; font-size: 0.72rem; cursor: pointer;">Copy</button>
                                        </span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #94a3b8;">Chủ tài khoản:</span>
                                        <span style="font-weight: 800; color: #fff;">NGO THI NINH</span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #94a3b8;">Số tiền:</span>
                                        <span style="display: flex; align-items: center; gap: 6px;">
                                            <b style="color: #34d399; font-size: 0.95rem;">150.000 VNĐ</b>
                                            <button onclick="navigator.clipboard.writeText('150000'); IELTSAuth.showSecurityToast('✓ Đã sao chép Số tiền: 150.000đ!');" style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.4); color: #34d399; border-radius: 4px; padding: 2px 6px; font-size: 0.72rem; cursor: pointer;">Copy</button>
                                        </span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px dashed #334155; margin-top: 4px; padding-top: 4px;">
                                        <span style="color: #94a3b8;">Nội dung CK:</span>
                                        <span style="display: flex; align-items: center; gap: 6px;">
                                            <b id="reg_transfer_memo" style="color: #f59e0b; font-family: monospace;">IELTS FD [SĐT_CỦA_BẠN]</b>
                                            <button onclick="navigator.clipboard.writeText(document.getElementById('reg_transfer_memo').innerText); IELTSAuth.showSecurityToast('✓ Đã sao chép Cú pháp chuyển khoản!');" style="background: rgba(245, 158, 11, 0.15); border: 1px solid rgba(245, 158, 11, 0.4); color: #fbbf24; border-radius: 4px; padding: 2px 6px; font-size: 0.72rem; cursor: pointer;">Copy</button>
                                        </span>
                                    </div>
                                </div>
                            </div>

                            <!-- Step 3: Fast Actions -->
                            <div style="display: flex; flex-direction: column; gap: 10px;">
                                <a id="reg_zalo_btn" href="https://zalo.me/0869669659" target="_blank" style="display: flex; align-items: center; justify-content: center; gap: 8px; width: 100%; box-sizing: border-box; background: linear-gradient(135deg, #0284c7, #0369a1); color: #fff; font-weight: 800; font-size: 0.92rem; padding: 13px; border-radius: 12px; text-decoration: none; box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);">
                                    📲 Nhắn Zalo Cô Ninh Để Nhận Mã Ngay (0869.669.659)
                                </a>
                                <button onclick="IELTSAuth.switchToActivateWithPrefill()" style="width: 100%; background: #334155; color: #e2e8f0; border: 1px solid #475569; font-weight: 700; font-size: 0.88rem; padding: 11px; border-radius: 10px; cursor: pointer;">
                                    🔑 Tôi đã có Mã Kích Hoạt $\rightarrow$ Chuyển sang Mở Khóa
                                </button>
                            </div>
                        </div>
                    </div>
                `;
                document.body.appendChild(modal);
            }
            modal.style.display = 'flex';
        },

        closePaywallModal: function () {
            const modal = document.getElementById('ielts_paywall_modal');
            if (modal) modal.style.display = 'none';
        },

        switchModalTab: function (tab) {
            const tabAct = document.getElementById('modal_tab_activate');
            const tabReg = document.getElementById('modal_tab_register');
            const btnAct = document.getElementById('tab_btn_activate');
            const btnReg = document.getElementById('tab_btn_register');
            if (tab === 'activate') {
                if (tabAct) tabAct.style.display = 'block';
                if (tabReg) tabReg.style.display = 'none';
                if (btnAct) { btnAct.style.borderBottomColor = '#38bdf8'; btnAct.style.color = '#38bdf8'; }
                if (btnReg) { btnReg.style.borderBottomColor = 'transparent'; btnReg.style.color = '#94a3b8'; }
            } else {
                if (tabAct) tabAct.style.display = 'none';
                if (tabReg) tabReg.style.display = 'block';
                if (btnAct) { btnAct.style.borderBottomColor = 'transparent'; btnAct.style.color = '#94a3b8'; }
                if (btnReg) { btnReg.style.borderBottomColor = '#38bdf8'; btnReg.style.color = '#38bdf8'; }
            }
        },

        submitActivation: function () {
            const name = (document.getElementById('auth_student_name')?.value || '').trim();
            const contact = (document.getElementById('auth_student_contact')?.value || '').trim();
            const key = (document.getElementById('auth_student_key')?.value || '').trim();
            const msgBox = document.getElementById('auth_msg_box');

            const res = this.activateStudent(name, contact, key);
            if (!res.success) {
                if (msgBox) {
                    msgBox.style.display = 'block';
                    msgBox.style.background = 'rgba(244, 63, 94, 0.2)';
                    msgBox.style.color = '#fb7185';
                    msgBox.style.border = '1px solid rgba(244, 63, 94, 0.4)';
                    msgBox.innerHTML = `⚠️ ${res.error}`;
                }
                return;
            }

            if (msgBox) {
                msgBox.style.display = 'block';
                msgBox.style.background = 'rgba(16, 185, 129, 0.2)';
                msgBox.style.color = '#34d399';
                msgBox.style.border = '1px solid rgba(16, 185, 129, 0.4)';
                msgBox.innerHTML = `🎉 KÍCH HOẠT THÀNH CÔNG!<br>Chào mừng <b>${res.profile.name}</b> đã tham gia <b>${res.profile.tierName}</b>!`;
            }

            setTimeout(() => {
                this.closePaywallModal();
                window.location.reload();
            }, 1200);
        },

        // --- 8.5 IELTS PASSPORT & LEARNING HUB (4-IN-1 DASHBOARD) ---
        getStreakData: function () {
            try {
                const raw = localStorage.getItem(STORAGE_KEY_STREAK);
                if (raw) return JSON.parse(raw);
            } catch (e) {}
            return { currentStreak: 1, lastDate: "", totalActiveDays: 1 };
        },

        updateStreak: function () {
            try {
                const streak = this.getStreakData();
                const today = new Date().toISOString().slice(0, 10);
                if (!streak.lastDate) {
                    streak.currentStreak = 1;
                    streak.lastDate = today;
                    streak.totalActiveDays = 1;
                } else if (streak.lastDate === today) {
                    // Already logged today
                } else {
                    const lastD = new Date(streak.lastDate);
                    const nowD = new Date(today);
                    const diffDays = Math.round((nowD - lastD) / (1000 * 60 * 60 * 24));
                    if (diffDays === 1) {
                        streak.currentStreak = (streak.currentStreak || 0) + 1;
                    } else if (diffDays > 1) {
                        streak.currentStreak = 1;
                    }
                    streak.lastDate = today;
                    streak.totalActiveDays = (streak.totalActiveDays || 0) + 1;
                }
                localStorage.setItem(STORAGE_KEY_STREAK, JSON.stringify(streak));
                return streak;
            } catch (e) {
                return { currentStreak: 1, lastDate: "", totalActiveDays: 1 };
            }
        },

        getTargetGoal: function () {
            try {
                const raw = localStorage.getItem(STORAGE_KEY_TARGET);
                if (raw) return JSON.parse(raw);
            } catch (e) {}
            return { targetBand: "7.0", targetDate: "2026-12", motto: "Consistency beats talent when talent doesn't work hard." };
        },

        saveTargetGoal: function (band, dateStr) {
            try {
                const cur = this.getTargetGoal();
                if (band) cur.targetBand = band;
                if (dateStr) cur.targetDate = dateStr;
                localStorage.setItem(STORAGE_KEY_TARGET, JSON.stringify(cur));
                this.showSecurityToast(`✓ Đã cập nhật mục tiêu: Band ${cur.targetBand} (${cur.targetDate})`);
                this.refreshPassportUI();
            } catch (e) {}
        },

        getMasterProgressSummary: function () {
            let unitsData = {};
            try {
                const raw = localStorage.getItem(STORAGE_KEY_MASTER_PROGRESS);
                if (raw) {
                    const parsed = JSON.parse(raw);
                    unitsData = parsed.units || {};
                }
            } catch (e) {}

            let completedCount = 0;
            let totalVocab = 0;
            let totalGrammar = 0;
            let listeningScores = [], readingScores = [];
            let writingCount = 0, speakingCount = 0;

            for (let u = 1; u <= 30; u++) {
                const k = (u < 10 ? "0" : "") + u;
                const d = unitsData[k];
                if (d) {
                    let hasActivity = false;
                    if (typeof d.vocab_score === 'number' && d.vocab_score > 0) {
                        totalVocab += d.vocab_score;
                        hasActivity = true;
                    }
                    if (typeof d.grammar_score === 'number' && d.grammar_score > 0) {
                        totalGrammar += d.grammar_score;
                        hasActivity = true;
                    }
                    if (typeof d.listening_score === 'number' && typeof d.listening_total === 'number' && d.listening_total > 0) {
                        listeningScores.push(d.listening_score / d.listening_total);
                        hasActivity = true;
                    }
                    if (typeof d.reading_score === 'number' && typeof d.reading_total === 'number' && d.reading_total > 0) {
                        readingScores.push(d.reading_score / d.reading_total);
                        hasActivity = true;
                    }
                    if (d.writing_completed) writingCount++;
                    if (d.speaking_completed) speakingCount++;
                    if (hasActivity) completedCount++;
                }
            }

            const listeningPct = listeningScores.length ? (listeningScores.reduce((a, b) => a + b, 0) / listeningScores.length) : 0;
            const readingPct = readingScores.length ? (readingScores.reduce((a, b) => a + b, 0) / readingScores.length) : 0;

            // Estimated Band calculation (Cambridge 4-skill formula)
            const lBand = listeningPct > 0 ? (4.0 + listeningPct * 4.0) : 4.5;
            const rBand = readingPct > 0 ? (4.0 + readingPct * 4.0) : 4.5;
            const wBand = writingCount >= 10 ? 6.5 : (writingCount >= 3 ? 5.5 : 5.0);
            const sBand = speakingCount >= 10 ? 6.5 : (speakingCount >= 3 ? 5.5 : 5.0);
            
            const rawAvg = (lBand + rBand + wBand + sBand) / 4.0;
            const estimatedBand = (Math.round(rawAvg * 2) / 2).toFixed(1);

            return {
                completedUnits: completedCount,
                percent: Math.round((completedCount / 30) * 100),
                totalVocabMastered: totalVocab,
                totalGrammarMastered: totalGrammar,
                listeningPct: Math.round(listeningPct * 100),
                readingPct: Math.round(readingPct * 100),
                writingCount: writingCount,
                speakingCount: speakingCount,
                estimatedBand: estimatedBand,
                lBand: lBand.toFixed(1),
                rBand: rBand.toFixed(1),
                wBand: wBand.toFixed(1),
                sBand: sBand.toFixed(1)
            };
        },

        // --- MISTAKE NOTEBOOK (SỔ TAY SỬA SAI) ---
        getMistakes: function () {
            try {
                const raw = localStorage.getItem(STORAGE_KEY_MISTAKES);
                if (raw) return JSON.parse(raw);
            } catch (e) {}
            return [];
        },

        saveMistakes: function (list) {
            try {
                localStorage.setItem(STORAGE_KEY_MISTAKES, JSON.stringify(list));
            } catch (e) {}
        },

        scanAndRecordMistakesFromDOM: function () {
            try {
                const unitId = window.CURRENT_UNIT_ID || (location.pathname.match(/unit_(\d+)/) ? location.pathname.match(/unit_(\d+)/)[1] : "FD");
                const wrongEls = document.querySelectorAll(".explanation.show.wrong");
                const correctEls = document.querySelectorAll(".explanation.show.correct");
                let mistakes = this.getMistakes();

                // 1. Remove mistakes that are now answered correctly
                correctEls.forEach(el => {
                    const item = el.closest(".question-item");
                    if (!item) return;
                    const qTitle = (item.querySelector(".question-title")?.innerText || "").trim();
                    if (qTitle) {
                        mistakes = mistakes.filter(m => !(m.unit === unitId && m.question === qTitle));
                    }
                });

                // 2. Add newly discovered mistakes
                wrongEls.forEach(el => {
                    const item = el.closest(".question-item");
                    if (!item) return;
                    const qTitle = (item.querySelector(".question-title")?.innerText || "").trim();
                    if (!qTitle) return;

                    const checkedRadio = item.querySelector("input[type='radio']:checked");
                    const userOptionText = checkedRadio ? (checkedRadio.closest(".option-label")?.innerText || "").trim() : "Chưa trả lời";

                    const options = [];
                    item.querySelectorAll(".option-label").forEach(lbl => {
                        options.push(lbl.innerText.trim());
                    });

                    const expText = el.innerText.replace(/^[✗✓xX]\s*(Sai rồi!|Chính xác!)\s*/i, "").trim();
                    const isVocab = (item.querySelector("input[name^='vocab']") !== null);
                    const type = isVocab ? "Từ vựng" : "Ngữ pháp";
                    const id = "MISTAKE_" + unitId + "_" + (isVocab ? "V" : "G") + "_" + Math.abs(this.hashCode(qTitle));

                    // Avoid duplicate
                    const idx = mistakes.findIndex(m => m.id === id);
                    const mistakeRecord = {
                        id: id,
                        unit: unitId,
                        type: type,
                        question: qTitle,
                        options: options,
                        userAns: userOptionText,
                        explanation: expText,
                        recordedAt: new Date().toISOString()
                    };

                    if (idx >= 0) {
                        mistakes[idx] = mistakeRecord;
                    } else {
                        mistakes.unshift(mistakeRecord);
                    }
                });

                this.saveMistakes(mistakes);
            } catch (e) {}
        },

        hashCode: function (str) {
            let h = 0;
            for (let i = 0; i < str.length; i++) {
                h = Math.imul(31, h) + str.charCodeAt(i) | 0;
            }
            return h;
        },

        removeMistake: function (id) {
            let mistakes = this.getMistakes();
            mistakes = mistakes.filter(m => m.id !== id);
            this.saveMistakes(mistakes);
            this.showSecurityToast("✓ Đã xóa câu hỏi khỏi Sổ tay sửa sai!");
            this.renderMistakesTabContent();
        },

        clearAllMistakes: function () {
            if (confirm("Bạn có chắc muốn làm sạch toàn bộ Sổ tay sửa sai?")) {
                this.saveMistakes([]);
                this.showSecurityToast("✓ Đã làm sạch Sổ tay sửa sai!");
                this.renderMistakesTabContent();
            }
        },

        // --- PASSPORT MODAL (UI/UX) ---
        openPassportModal: function (initialTab) {
            this.updateStreak();
            let modal = document.getElementById("ielts_passport_modal");
            if (!modal) {
                modal = document.createElement("div");
                modal.id = "ielts_passport_modal";
                modal.style.cssText = `
                    position: fixed;
                    inset: 0;
                    background: rgba(11, 17, 32, 0.88);
                    backdrop-filter: blur(14px);
                    z-index: 10000001;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 14px;
                    overflow-y: auto;
                    font-family: 'Plus Jakarta Sans', sans-serif;
                `;
                document.body.appendChild(modal);
            }

            modal.innerHTML = this.buildPassportModalHtml();
            modal.style.display = "flex";
            this.switchPassportTab(initialTab || "passport");
        },

        closePassportModal: function () {
            const modal = document.getElementById("ielts_passport_modal");
            if (modal) modal.style.display = "none";
        },

        switchPassportTab: function (tab) {
            const tabs = ["passport", "radar", "mistakes"];
            tabs.forEach(t => {
                const sec = document.getElementById("passport_tab_content_" + t);
                const btn = document.getElementById("passport_btn_" + t);
                if (sec) sec.style.display = (t === tab) ? "block" : "none";
                if (btn) {
                    if (t === tab) {
                        btn.style.borderBottomColor = "#38bdf8";
                        btn.style.color = "#38bdf8";
                        btn.style.background = "rgba(56, 189, 248, 0.08)";
                    } else {
                        btn.style.borderBottomColor = "transparent";
                        btn.style.color = "#94a3b8";
                        btn.style.background = "none";
                    }
                }
            });

            if (tab === "mistakes") {
                this.renderMistakesTabContent();
            }
        },

        refreshPassportUI: function () {
            const modal = document.getElementById("ielts_passport_modal");
            if (modal && modal.style.display === "flex") {
                modal.innerHTML = this.buildPassportModalHtml();
                this.switchPassportTab("passport");
            }
        },

        buildPassportModalHtml: function () {
            const isOwner = this.isAdminOwner();
            const student = this.getStudent();
            const streak = this.getStreakData();
            const target = this.getTargetGoal();
            const progress = this.getMasterProgressSummary();

            let displayName = "Học Viên Trải Nghiệm (Guest)";
            let displayKey = "NINH-TRIAL-DEMO";
            let displayTier = "Bản Học Thử Miễn Phí (Unit 01-02)";
            let badgeTitle = "🌱 Foundation Explorer";

            if (isOwner) {
                displayName = "Cô Ninh (Chủ Sở Hữu Website)";
                displayKey = "NINH-VIP-8888-25A9";
                displayTier = "VIP Toàn Quyền Quản Trị Hệ Thống";
                badgeTitle = "👑 Master Admin & Head Coach";
            } else if (student) {
                displayName = student.name;
                displayKey = student.key;
                displayTier = student.tierName;
                badgeTitle = (student.tier === 'VIP') ? "👑 IELTS VIP Scholar" : "🎯 IELTS Foundation Candidate";
            }

            const targetDiff = (parseFloat(target.targetBand) - parseFloat(progress.estimatedBand)).toFixed(1);
            const targetDiffText = targetDiff > 0 ? `(Cách mục tiêu: +${targetDiff} Band)` : `(Đạt hoặc vượt mục tiêu!)`;

            return `
                <div style="background: #1e293b; border: 1.5px solid rgba(197, 139, 98, 0.45); border-radius: 24px; max-width: 680px; width: 100%; box-shadow: 0 25px 60px rgba(0,0,0,0.85), 0 0 35px rgba(197, 139, 98, 0.25); overflow: hidden; animation: popIn 0.22s ease-out; color: #f8fafc; max-height: 92vh; display: flex; flex-direction: column;">
                    
                    <!-- Header -->
                    <div style="padding: 16px 22px; background: linear-gradient(135deg, rgba(30, 41, 59, 1), rgba(15, 23, 42, 1)); border-bottom: 1px solid rgba(197, 139, 98, 0.3); display: flex; justify-content: space-between; align-items: center; flex-shrink: 0;">
                        <div style="display: flex; align-items: center; gap: 12px;">
                            <div style="width: 42px; height: 42px; border-radius: 12px; background: radial-gradient(circle, rgba(197, 139, 98, 0.3) 0%, rgba(15, 23, 42, 0.9) 100%); border: 1.5px solid #c58b62; display: flex; align-items: center; justify-content: center; font-size: 22px;">🪷</div>
                            <div>
                                <div style="font-size: 0.75rem; color: #c58b62; font-weight: 800; letter-spacing: 1px; text-transform: uppercase;">IELTS Journey with Ms Ninh</div>
                                <div style="font-size: 1.15rem; color: #fff; font-weight: 800; font-family: 'Space Grotesk', sans-serif;">Hồ Sơ Năng Lực & IELTS Passport</div>
                            </div>
                        </div>
                        <button onclick="IELTSAuth.closePassportModal()" style="background: none; border: none; color: #94a3b8; font-size: 26px; cursor: pointer; padding: 4px 8px; line-height: 1;">&times;</button>
                    </div>

                    <!-- Navigation Tabs -->
                    <div style="display: flex; border-bottom: 1px solid #334155; background: #0f172a; flex-shrink: 0;">
                        <button id="passport_btn_passport" onclick="IELTSAuth.switchPassportTab('passport')" style="flex: 1; padding: 13px 8px; background: none; border: none; border-bottom: 2px solid #38bdf8; color: #38bdf8; font-weight: 700; font-size: 0.85rem; cursor: pointer; transition: all 0.2s;">
                            👤 Thẻ Học Viên VIP
                        </button>
                        <button id="passport_btn_radar" onclick="IELTSAuth.switchPassportTab('radar')" style="flex: 1; padding: 13px 8px; background: none; border: none; border-bottom: 2px solid transparent; color: #94a3b8; font-weight: 700; font-size: 0.85rem; cursor: pointer; transition: all 0.2s;">
                            📊 Radar 4 Kỹ Năng
                        </button>
                        <button id="passport_btn_mistakes" onclick="IELTSAuth.switchPassportTab('mistakes')" style="flex: 1; padding: 13px 8px; background: none; border: none; border-bottom: 2px solid transparent; color: #94a3b8; font-weight: 700; font-size: 0.85rem; cursor: pointer; transition: all 0.2s;">
                            📕 Sổ Tay Sửa Sai
                        </button>
                    </div>

                    <!-- Body Content (Scrollable) -->
                    <div style="padding: 20px 22px; overflow-y: auto; flex: 1;">

                        <!-- TAB 1: THẺ HỌC VIÊN & MỤC TIÊU -->
                        <div id="passport_tab_content_passport">
                            <!-- Digital Passport Card (Hologram Look) -->
                            <div style="background: radial-gradient(circle at 10% 20%, rgba(56, 189, 248, 0.15) 0%, rgba(15, 23, 42, 0.98) 85%); border: 1.5px solid rgba(197, 139, 98, 0.55); border-radius: 20px; padding: 20px; margin-bottom: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.6), inset 0 0 20px rgba(197, 139, 98, 0.15); position: relative; overflow: hidden;">
                                <div style="position: absolute; right: -25px; bottom: -25px; font-size: 110px; opacity: 0.05; pointer-events: none; user-select: none;">🪷</div>

                                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px; flex-wrap: wrap; gap: 10px;">
                                    <div>
                                        <div style="font-size: 0.72rem; font-weight: 800; color: #c58b62; text-transform: uppercase; letter-spacing: 1.2px;">ACADEMIC PASSPORT • OFFICIAL MEMBER</div>
                                        <div style="font-size: 1.35rem; font-weight: 800; color: #fff; margin-top: 3px;">${displayName}</div>
                                        <div style="font-size: 0.78rem; color: #94a3b8; font-family: monospace; margin-top: 2px;">ID: <span style="color: #38bdf8;">${displayKey}</span></div>
                                    </div>
                                    <div style="text-align: right;">
                                        <span style="display: inline-block; background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); color: #34d399; font-size: 0.75rem; padding: 4px 10px; border-radius: 999px; font-weight: 800;">
                                            ${badgeTitle}
                                        </span>
                                        <div style="font-size: 0.75rem; color: #94a3b8; margin-top: 4px;">Khóa: <b>${displayTier}</b></div>
                                    </div>
                                </div>

                                <!-- Streak & Goal Grid -->
                                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 12px; margin-top: 14px;">
                                    <div style="background: rgba(11, 17, 32, 0.75); border: 1px solid #334155; border-radius: 12px; padding: 12px; text-align: center;">
                                        <div style="font-size: 1.5rem; margin-bottom: 2px;">🔥</div>
                                        <div style="font-size: 1.25rem; font-weight: 800; color: #fbbf24;">${streak.currentStreak} Ngày</div>
                                        <div style="font-size: 0.7rem; color: #94a3b8; text-transform: uppercase;">Chuỗi học liên tục</div>
                                    </div>
                                    <div style="background: rgba(11, 17, 32, 0.75); border: 1px solid #334155; border-radius: 12px; padding: 12px; text-align: center;">
                                        <div style="font-size: 1.5rem; margin-bottom: 2px;">🎯</div>
                                        <div style="font-size: 1.25rem; font-weight: 800; color: #38bdf8;">Band ${target.targetBand}</div>
                                        <div style="font-size: 0.7rem; color: #94a3b8; text-transform: uppercase;">Mục tiêu cá nhân</div>
                                    </div>
                                    <div style="background: rgba(11, 17, 32, 0.75); border: 1px solid #334155; border-radius: 12px; padding: 12px; text-align: center;">
                                        <div style="font-size: 1.5rem; margin-bottom: 2px;">⏳</div>
                                        <div style="font-size: 1.25rem; font-weight: 800; color: #c58b62;">${target.targetDate}</div>
                                        <div style="font-size: 0.7rem; color: #94a3b8; text-transform: uppercase;">Hạn định thi</div>
                                    </div>
                                </div>
                            </div>

                            <!-- Goal Setting Form -->
                            <div style="background: #0f172a; border: 1px solid #334155; border-radius: 16px; padding: 16px; margin-bottom: 20px;">
                                <div style="font-size: 0.85rem; font-weight: 800; color: #38bdf8; margin-bottom: 12px;">
                                    🎯 Cài Đặt Mục Tiêu Của Bạn
                                </div>
                                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                                    <div>
                                        <label style="display: block; font-size: 0.78rem; font-weight: 700; color: #cbd5e1; margin-bottom: 5px;">Mục Tiêu Target Band</label>
                                        <select id="cfg_target_band" onchange="IELTSAuth.saveTargetGoal(this.value, null)" style="width: 100%; box-sizing: border-box; background: #0b1120; border: 1px solid #334155; border-radius: 8px; padding: 9px 12px; color: #fff; font-size: 0.88rem;">
                                            <option value="6.0" ${target.targetBand === '6.0' ? 'selected' : ''}>Band 6.0 (Foundation Mastery)</option>
                                            <option value="6.5" ${target.targetBand === '6.5' ? 'selected' : ''}>Band 6.5 (Competent Academic)</option>
                                            <option value="7.0" ${target.targetBand === '7.0' ? 'selected' : ''}>Band 7.0 (Good User)</option>
                                            <option value="7.5" ${target.targetBand === '7.5' ? 'selected' : ''}>Band 7.5 (Advanced)</option>
                                            <option value="8.0" ${target.targetBand === '8.0' ? 'selected' : ''}>Band 8.0+ (Superior Mastery)</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label style="display: block; font-size: 0.78rem; font-weight: 700; color: #cbd5e1; margin-bottom: 5px;">Thời Gian Dự Thi</label>
                                        <input type="text" id="cfg_target_date" value="${target.targetDate}" placeholder="Ví dụ: Tháng 12/2026" onchange="IELTSAuth.saveTargetGoal(null, this.value)" style="width: 100%; box-sizing: border-box; background: #0b1120; border: 1px solid #334155; border-radius: 8px; padding: 9px 12px; color: #fff; font-size: 0.88rem;">
                                    </div>
                                </div>
                            </div>

                            <!-- Ms Ninh's Coaching Motto -->
                            <div style="background: rgba(197, 139, 98, 0.12); border-left: 4px solid #c58b62; border-radius: 0 12px 12px 0; padding: 14px 16px; font-size: 0.84rem; line-height: 1.6; color: #e2e8f0;">
                                <div style="font-weight: 800; color: #c58b62; margin-bottom: 4px;">💌 Lời Nhắn Từ Cô Ninh:</div>
                                <i>"Mỗi ngày một chút đều đặn chính là bí quyết giúp học viên của cô chinh phục Band 8.0+. Hãy duy trì ngọn lửa 🔥 Streak và làm chủ từng Unit nhé!"</i>
                            </div>
                        </div>

                        <!-- TAB 2: RADAR 4 KỸ NĂNG & TIẾN ĐỘ 30 UNITS -->
                        <div id="passport_tab_content_radar" style="display: none;">
                            <!-- Estimated Band Card -->
                            <div style="background: linear-gradient(135deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.95)); border: 1.5px solid rgba(56, 189, 248, 0.5); border-radius: 20px; padding: 18px 20px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
                                <div>
                                    <div style="font-size: 0.72rem; font-weight: 800; color: #38bdf8; text-transform: uppercase; letter-spacing: 1px;">DỰ PHÓNG BAND ĐIỂM CAMBRIDGE</div>
                                    <div style="display: flex; align-items: baseline; gap: 8px; margin-top: 4px;">
                                        <span style="font-size: 2.2rem; font-weight: 800; color: #34d399; font-family: 'Space Grotesk', sans-serif;">Band ${progress.estimatedBand}</span>
                                        <span style="font-size: 0.85rem; color: #94a3b8;">${targetDiffText}</span>
                                    </div>
                                    <div style="font-size: 0.75rem; color: #cbd5e1; margin-top: 2px;">Dựa trên phân tích kết quả bài tập & test của các Unit đã học.</div>
                                </div>
                                <div style="text-align: right;">
                                    <button onclick="IELTSAuth.openPaywallModal()" style="background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8; padding: 8px 14px; border-radius: 10px; font-weight: 700; font-size: 0.8rem; cursor: pointer;">
                                        Mở Khóa Toàn Bộ 30 Unit ➔
                                    </button>
                                </div>
                            </div>

                            <!-- 30 Units Progress Bar -->
                            <div style="background: #0f172a; border: 1px solid #334155; border-radius: 16px; padding: 16px; margin-bottom: 20px;">
                                <div style="display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 700; margin-bottom: 8px;">
                                    <span>Tiến Độ Chinh Phục 30 Units Foundation</span>
                                    <span style="color: #38bdf8;">${progress.completedUnits}/30 Units (${progress.percent}%)</span>
                                </div>
                                <div style="background: #1e293b; height: 10px; border-radius: 999px; overflow: hidden;">
                                    <div style="width: ${progress.percent}%; height: 100%; background: linear-gradient(90deg, #38bdf8, #10b981); border-radius: 999px; transition: width 0.4s ease;"></div>
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 0.75rem; color: #94a3b8; margin-top: 8px;">
                                    <span>Vốn từ học thuật đã nạp: <b style="color: #34d399;">${progress.totalVocabMastered} / 450 từ</b></span>
                                    <span>Điểm ngữ pháp vững vàng: <b style="color: #fbbf24;">${progress.totalGrammarMastered} điểm</b></span>
                                </div>
                            </div>

                            <!-- 4 Skills Breakdown Grid -->
                            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(135px, 1fr)); gap: 12px;">
                                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 14px; padding: 14px;">
                                    <div style="font-size: 1.2rem; margin-bottom: 4px;">🎧</div>
                                    <div style="font-size: 0.78rem; font-weight: 700; color: #38bdf8; text-transform: uppercase;">Listening Lab</div>
                                    <div style="font-size: 1.3rem; font-weight: 800; color: #fff; margin: 4px 0;">Band ${progress.lBand}</div>
                                    <div style="font-size: 0.72rem; color: #94a3b8;">Độ chính xác: ${progress.listeningPct}%</div>
                                </div>
                                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 14px; padding: 14px;">
                                    <div style="font-size: 1.2rem; margin-bottom: 4px;">📖</div>
                                    <div style="font-size: 0.78rem; font-weight: 700; color: #10b981; text-transform: uppercase;">Reading Lab</div>
                                    <div style="font-size: 1.3rem; font-weight: 800; color: #fff; margin: 4px 0;">Band ${progress.rBand}</div>
                                    <div style="font-size: 0.72rem; color: #94a3b8;">Độ chính xác: ${progress.readingPct}%</div>
                                </div>
                                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 14px; padding: 14px;">
                                    <div style="font-size: 1.2rem; margin-bottom: 4px;">✍️</div>
                                    <div style="font-size: 0.78rem; font-weight: 700; color: #f59e0b; text-transform: uppercase;">Writing Lab</div>
                                    <div style="font-size: 1.3rem; font-weight: 800; color: #fff; margin: 4px 0;">Band ${progress.wBand}</div>
                                    <div style="font-size: 0.72rem; color: #94a3b8;">Đã nộp: ${progress.writingCount} bài luận</div>
                                </div>
                                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 14px; padding: 14px;">
                                    <div style="font-size: 1.2rem; margin-bottom: 4px;">🗣️</div>
                                    <div style="font-size: 0.78rem; font-weight: 700; color: #a855f7; text-transform: uppercase;">Speaking Lab</div>
                                    <div style="font-size: 1.3rem; font-weight: 800; color: #fff; margin: 4px 0;">Band ${progress.sBand}</div>
                                    <div style="font-size: 0.72rem; color: #94a3b8;">Thu âm: ${progress.speakingCount} lượt</div>
                                </div>
                            </div>
                        </div>

                        <!-- TAB 3: SỔ TAY SỬA SAI (MISTAKE NOTEBOOK) -->
                        <div id="passport_tab_content_mistakes" style="display: none;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
                                <div>
                                    <div style="font-size: 0.95rem; font-weight: 800; color: #fff;">Sổ Tay Lỗi Sai Tự Động (Spaced Repetition)</div>
                                    <div style="font-size: 0.75rem; color: #94a3b8;">Tự động gom lại các câu bạn chọn sai trong các bài Test Từ Vựng & Ngữ Pháp.</div>
                                </div>
                                <button onclick="IELTSAuth.clearAllMistakes()" style="background: rgba(244, 63, 94, 0.15); border: 1px solid rgba(244, 63, 94, 0.4); color: #fb7185; padding: 6px 10px; border-radius: 8px; font-size: 0.75rem; font-weight: 700; cursor: pointer;">
                                    Làm Sạch Sổ Tay 🗑️
                                </button>
                            </div>
                            <div id="mistakes_container_list">
                                <!-- Dynamic Rendered via renderMistakesTabContent() -->
                            </div>
                        </div>

                    </div>
                </div>
            `;
        },

        renderMistakesTabContent: function () {
            const container = document.getElementById("mistakes_container_list");
            if (!container) return;
            const mistakes = this.getMistakes();

            if (mistakes.length === 0) {
                container.innerHTML = `
                    <div style="background: #0f172a; border: 1.5px dashed #334155; border-radius: 16px; padding: 36px 20px; text-align: center; color: #94a3b8;">
                        <div style="font-size: 38px; margin-bottom: 8px;">🎉</div>
                        <div style="font-size: 0.95rem; font-weight: 800; color: #34d399; margin-bottom: 4px;">Hiện Tại Bạn Chưa Có Câu Sai Nào!</div>
                        <div style="font-size: 0.78rem; max-width: 400px; margin: 0 auto; line-height: 1.5;">
                            Khi bạn làm bài Test Từ Vựng (20 câu) hoặc Test Ngữ Pháp (10 câu) trong bất kỳ Unit nào, hệ thống sẽ tự động lưu các câu làm sai vào đây để bạn ôn luyện lại riêng biệt.
                        </div>
                    </div>
                `;
                return;
            }

            container.innerHTML = `
                <div style="font-size: 0.78rem; color: #fbbf24; font-weight: 700; margin-bottom: 12px; background: rgba(245, 158, 11, 0.12); padding: 8px 12px; border-radius: 8px; border: 1px solid rgba(245, 158, 11, 0.3);">
                    ⚠️ Bạn đang có ${mistakes.length} câu cần củng cố lại. Hãy bấm 'Luyện Lại' hoặc 'Hỏi Cô Ninh' để ghi nhớ bản chất nhé!
                </div>
                <div style="display: flex; flex-direction: column; gap: 12px;">
                    ${mistakes.map((m, idx) => `
                        <div style="background: #0f172a; border: 1px solid rgba(244, 63, 94, 0.35); border-radius: 14px; padding: 14px 16px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <span style="background: rgba(56, 189, 248, 0.15); color: #38bdf8; font-size: 0.72rem; padding: 2px 8px; border-radius: 999px; font-weight: 800;">Unit ${m.unit}</span>
                                    <span style="background: rgba(197, 139, 98, 0.2); color: #c58b62; font-size: 0.72rem; padding: 2px 8px; border-radius: 999px; font-weight: 800;">${m.type}</span>
                                </div>
                                <button onclick="IELTSAuth.removeMistake('${m.id}')" style="background: none; border: none; color: #64748b; font-size: 0.75rem; cursor: pointer;" title="Đã thuộc bài, xóa câu này">✕ Đã Thuộc</button>
                            </div>
                            <div style="font-size: 0.88rem; font-weight: 700; color: #fff; margin-bottom: 8px;">${m.question}</div>
                            <div style="background: #0b1120; border-radius: 8px; padding: 8px 10px; font-size: 0.78rem; line-height: 1.6; margin-bottom: 10px;">
                                <div style="color: #fb7185;">✗ Bạn đã chọn: <b>${m.userAns}</b></div>
                                <div style="color: #34d399; margin-top: 2px;">💡 Giải thích: <i>${m.explanation}</i></div>
                            </div>
                            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                                <a href="https://zalo.me/0869669659?text=${encodeURIComponent('Chào Cô Ninh, em đang ôn lại câu hỏi này trong Unit ' + m.unit + ' nhưng chưa hiểu rõ: "' + m.question + '". Nhờ cô giải thích thêm giúp em với ạ!')}" target="_blank" style="display: inline-flex; align-items: center; gap: 6px; background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8; padding: 6px 12px; border-radius: 8px; font-size: 0.75rem; font-weight: 700; text-decoration: none;">
                                    💬 Nhờ Cô Ninh Giải Thích Qua Zalo
                                </a>
                            </div>
                        </div>
                    `).join("")}
                </div>
            `;
        },

        // --- 9. RENDER MEMBER STATUS BAR (ON INDEX) ---
        renderMemberStatusBar: function (containerId) {
            const container = document.getElementById(containerId);
            if (!container) return;

            // 1. MASTER ADMIN OWNER BAR
            if (this.isAdminOwner()) {
                container.innerHTML = `
                    <div style="display: flex; align-items: center; justify-content: space-between; background: radial-gradient(circle at 10% 20%, rgba(197, 139, 98, 0.2) 0%, rgba(30, 41, 59, 0.98) 75%); border: 1.5px solid rgba(197, 139, 98, 0.55); border-radius: 14px; padding: 12px 18px; margin-bottom: 20px; box-shadow: 0 6px 25px rgba(0,0,0,0.5), 0 0 15px rgba(197, 139, 98, 0.2); flex-wrap: wrap; gap: 10px;">
                        <div style="display: flex; align-items: center; gap: 12px;">
                            <span style="font-size: 1.6rem;">👑</span>
                            <div>
                                <div style="font-size: 0.92rem; color: #fff; font-weight: 800;">
                                    Xin chào <span style="color: #c58b62;">Cô Ninh (Chủ Sở Hữu Website)</span>
                                    <span style="display: inline-block; background: rgba(197, 139, 98, 0.2); color: #c58b62; border: 1px solid rgba(197, 139, 98, 0.45); font-size: 0.72rem; padding: 2px 8px; border-radius: 999px; margin-left: 6px; font-weight: 800;">MASTER ADMIN</span>
                                </div>
                                <div style="font-size: 0.76rem; color: #94a3b8;">
                                    Thiết bị này đã được mở khóa toàn quyền 30 Units & Full tính năng.
                                </div>
                            </div>
                        </div>
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <a href="admin.html" style="background: linear-gradient(135deg, #38bdf8, #0284c7); color: #0b1120; font-size: 0.82rem; font-weight: 800; padding: 8px 16px; border-radius: 10px; text-decoration: none; box-shadow: 0 0 12px rgba(56, 189, 248, 0.35);">
                                ⚙️ Quản Trị Học Viên
                            </a>
                            <button onclick="IELTSAuth.setAdminOwner(false); location.reload();" style="background: rgba(51, 65, 85, 0.8); border: 1px solid #475569; color: #cbd5e1; font-size: 0.78rem; font-weight: 700; padding: 8px 12px; border-radius: 10px; cursor: pointer;" title="Tạm thời chuyển sang chế độ khách để kiểm tra giao diện">
                                👁️ Xem Dưới Góc Nhìn Khách
                            </button>
                        </div>
                    </div>
                `;
                return;
            }

            const student = this.getStudent();
            if (student && !student.isDeviceMismatch) {
                container.innerHTML = `
                    <div style="display: flex; align-items: center; justify-content: space-between; background: var(--surface-color, #ffffff); border: 1.5px solid var(--border, #eadccb); box-shadow: var(--card-shadow, 0 4px 18px rgba(20, 50, 77, 0.06)); color: var(--text-main, #14324d); border-radius: 14px; padding: 12px 18px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.4); flex-wrap: wrap; gap: 10px;">
                        <div style="display: flex; align-items: center; gap: 10px; cursor: pointer;" onclick="IELTSAuth.openPassportModal()">
                            <span style="font-size: 1.5rem;">🎓</span>
                            <div>
                                <div style="font-size: 0.88rem; color: #fff; font-weight: 700;">
                                    Học viên: <span style="color: #38bdf8;">${student.name}</span>
                                    <span style="display: inline-block; background: rgba(16, 185, 129, 0.2); color: #34d399; font-size: 0.72rem; padding: 2px 8px; border-radius: 999px; margin-left: 6px; font-weight: 800;">✓ ĐÃ KÍCH HOẠT</span>
                                    <span style="display: inline-block; background: rgba(245, 158, 11, 0.2); color: #fbbf24; font-size: 0.72rem; padding: 2px 8px; border-radius: 999px; margin-left: 4px; font-weight: 800;">🔥 ${this.getStreakData().currentStreak} Ngày</span>
                                </div>
                                <div style="font-size: 0.75rem; color: #94a3b8;">
                                    Gói học: <b style="color: #cbd5e1;">${student.tierName}</b> • Mục tiêu: <b style="color: #38bdf8;">Band ${this.getTargetGoal().targetBand}</b> • <i>Bấm để xem Bảng Năng Lực & Sổ Tay ➔</i>
                                </div>
                            </div>
                        </div>
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <button onclick="IELTSAuth.toggleTheme()" class="theme-switch-pill" style="display: inline-flex; align-items: center; gap: 5px; background: rgba(197, 133, 93, 0.15); border: 1.5px solid rgba(197, 133, 93, 0.45); color: var(--accent, #c5855d); padding: 6px 12px; border-radius: 999px; font-size: 0.78rem; font-weight: 700; cursor: pointer;">☀️ <span class="theme-text">Giấy Ngà</span></button>
                            <button onclick="IELTSAuth.openPassportModal()" style="background: linear-gradient(135deg, #14324d, #1d4367); color: #fff; color: #0b1120; font-size: 0.8rem; font-weight: 800; padding: 7px 14px; border-radius: 10px; border: none; cursor: pointer; box-shadow: 0 0 12px rgba(56, 189, 248, 0.35);">
                                🎓 Bảng Năng Lực & Sổ Tay
                            </button>
                            <button onclick="IELTSAuth.openPaywallModal()" style="background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8; font-size: 0.78rem; font-weight: 700; padding: 6px 12px; border-radius: 8px; cursor: pointer;">
                                🔑 Nhập Mã Khác
                            </button>
                            <button onclick="if(confirm('Bạn có chắc muốn đăng xuất khỏi thiết bị này?')) IELTSAuth.logout();" style="background: rgba(244, 63, 94, 0.15); border: 1px solid rgba(244, 63, 94, 0.4); color: #fb7185; font-size: 0.78rem; font-weight: 700; padding: 6px 12px; border-radius: 8px; cursor: pointer;">
                                Đăng Xuất
                            </button>
                        </div>
                    </div>
                `;
            } else {
                container.innerHTML = `
                    <div style="display: flex; align-items: center; justify-content: space-between; background: var(--surface-color, #ffffff); border: 1.5px solid var(--border, #eadccb); box-shadow: var(--card-shadow, 0 4px 18px rgba(20, 50, 77, 0.06)); color: var(--text-main, #14324d); border-radius: 14px; padding: 12px 18px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.4); flex-wrap: wrap; gap: 10px;">
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <span style="font-size: 1.4rem;">✨</span>
                            <div>
                                <div style="font-size: 0.88rem; color: #fff; font-weight: 700;">
                                    Cổng Học Tập & Bản Quyền Hệ Thống
                                    <span style="display: inline-block; background: rgba(56, 189, 248, 0.2); color: #38bdf8; font-size: 0.72rem; padding: 2px 8px; border-radius: 999px; margin-left: 6px; font-weight: 800;">HỌC THỬ FREE: UNIT 01 & 02</span>
                                </div>
                                <div style="font-size: 0.75rem; color: #94a3b8;">
                                    Học viên đã đăng ký vui lòng bấm Kích Hoạt để mở khóa toàn bộ 30 Units.
                                </div>
                            </div>
                        </div>
                        <button onclick="IELTSAuth.openPaywallModal()" style="background: linear-gradient(135deg, #38bdf8, #0284c7); color: #0b1120; border: none; font-size: 0.84rem; font-weight: 800; padding: 8px 16px; border-radius: 10px; cursor: pointer; box-shadow: 0 0 15px rgba(56, 189, 248, 0.35);">
                            🔑 Nhập Mã Kích Hoạt / Đăng Ký
                        </button>
                    </div>
                `;
            }
        }
    };

    window.IELTSAuth = IELTSAuth;

    // Secret Admin Click Trigger (Click avatar 3 times in 1.5s to unlock)
    let _avatarClicks = 0, _avatarTimer = null;
    document.addEventListener('click', function(e) {
        if (e.target && (e.target.classList.contains('brand-avatar-img') || e.target.closest('.brand-avatar-img'))) {
            _avatarClicks++;
            clearTimeout(_avatarTimer);
            _avatarTimer = setTimeout(function() { _avatarClicks = 0; }, 1200);
            if (_avatarClicks >= 3) {
                _avatarClicks = 0;
                const pass = prompt("🔐 XÁC THỰC CHỦ SỞ HỮU WEBSITE:\nVui lòng nhập Mật Khẩu Quản Trị Viên (Admin Passkey) của Cô Ninh:");
                if (pass === "NINH2026ADMIN") {
                    IELTSAuth.setAdminOwner(true);
                    alert("🎉 Xác thực thành công! Xin chào Cô Ninh.\nToàn bộ hệ thống 30 Unit đã được mở khóa toàn quyền trên thiết bị này.");
                    window.location.reload();
                } else if (pass !== null) {
                    alert("Mật khẩu quản trị viên không chính xác!");
                }
            }
        }
    });

    // Auto-initialize anti-theft shield
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => IELTSAuth.initAntiTheft());
    } else {
        IELTSAuth.initTheme();
        IELTSAuth.initAntiTheft();
    }


    // Auto-update daily streak on script load
    try { IELTSAuth.updateStreak(); } catch (e) {}

    // Auto-scan mistakes when students grade quizzes in any unit
    document.addEventListener('click', function(e) {
        const btn = e.target.closest('button');
        if (btn) {
            const oc = btn.getAttribute('onclick') || '';
            if (oc.includes('gradeVocabTest') || oc.includes('gradeGrammarTest') || oc.includes('gradeQuiz')) {
                setTimeout(function() {
                    if (window.IELTSAuth && window.IELTSAuth.scanAndRecordMistakesFromDOM) {
                        window.IELTSAuth.scanAndRecordMistakesFromDOM();
                    }
                }, 200);
            }
        }
    });

})(window);
