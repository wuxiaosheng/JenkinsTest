LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_SHORT_COMMANDS := true

LOCAL_MODULE := cocos2djs_shared

LOCAL_MODULE_FILENAME := libcocos2djs

LOCAL_SRC_FILES := hellojavascript/main.cpp \
                   ../../../Classes/AppDelegate.cpp 

LOCAL_C_INCLUDES := $(LOCAL_PATH)/../../../Classes

LOCAL_STATIC_LIBRARIES := cocos2d_js_static

LOCAL_EXPORT_CFLAGS := -DCOCOS2D_DEBUG=2 -DCOCOS2D_JAVASCRIPT

include $(BUILD_SHARED_LIBRARY)

$(call import-add-path,$(LOCAL_PATH)/../../../../cocos2d-x)
$(call import-add-path,$(LOCAL_PATH)/../../../../cocos2d-x/external)
$(call import-add-path,$(LOCAL_PATH)/../../../../cocos2d-x/cocos)
$(call import-module, scripting/js-bindings/proj.android)
